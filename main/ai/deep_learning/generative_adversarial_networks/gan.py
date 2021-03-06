import os
import time
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torch.autograd as autograd
from torch.autograd import Variable
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from discriminator import Discriminator
from generator import Generator

transform_train = transforms.Compose([
    transforms.RandomResizedCrop(32, scale=(0.7, 1.0), ratio=(1.0, 1.0)),
    transforms.ColorJitter(brightness=0.1 * torch.randn(1),
                           contrast=0.1 * torch.randn(1),
                           saturation=0.1 * torch.randn(1),
                           hue=0.1 * torch.randn(1)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

transform_test = transforms.Compose([
    transforms.CenterCrop(32),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

batch_size = 128

trainset = datasets.CIFAR10(root='./',
                            train=True,
                            download=True,
                            transform=transform_train)
trainloader = data.DataLoader(trainset,
                              batch_size=batch_size,
                              shuffle=True,
                              num_workers=8)

testset = datasets.CIFAR10(root='./',
                           train=False,
                           download=False,
                           transform=transform_test)
testloader = data.DataLoader(testset,
                             batch_size=batch_size,
                             shuffle=False,
                             num_workers=8)


def avoidOverflow(optimizer):
    for group in optimizer.param_groups:
        for p in group['params']:
            state = optimizer.state[p]
            if 'step' in state and state['step'] >= 1024:
                state['step'] = 1000


def plot(samples):
    fig = plt.figure(figsize=(10, 10))
    gs = gridspec.GridSpec(10, 10)
    gs.update(wspace=0.02, hspace=0.02)

    for i, sample in enumerate(samples):
        ax = plt.subplot(gs[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('equal')
        plt.imshow(sample)
    return fig


def calc_gradient_penalty(netD, real_data, fake_data):
    DIM = 32
    LAMBDA = 10
    alpha = torch.rand(batch_size, 1)
    alpha = alpha.expand(batch_size,
                         int(real_data.nelement() / batch_size)).contiguous()
    alpha = alpha.view(batch_size, 3, DIM, DIM)
    alpha = alpha.cuda()

    fake_data = fake_data.view(batch_size, 3, DIM, DIM)
    interpolates = alpha * real_data.detach() + (
        (1 - alpha) * fake_data.detach())

    interpolates = interpolates.cuda()
    interpolates.requires_grad_(True)

    disc_interpolates, _ = netD(interpolates)

    gradients = autograd.grad(outputs=disc_interpolates,
                              inputs=interpolates,
                              grad_outputs=torch.ones(
                                  disc_interpolates.size()).cuda(),
                              create_graph=True,
                              retain_graph=True,
                              only_inputs=True)[0]

    gradients = gradients.view(gradients.size(0), -1)
    gradient_penalty = ((gradients.norm(2, dim=1) - 1)**2).mean() * LAMBDA
    return gradient_penalty


def train_D_Without_G():
    model = Discriminator()
    model.cuda()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
    learning_rate = 0.0001
    for epoch in range(100):
        avoidOverflow(optimizer)
        if (epoch == 50):
            for param_group in optimizer.param_groups:
                param_group['lr'] = learning_rate / 10.0
        if (epoch == 75):
            for param_group in optimizer.param_groups:
                param_group['lr'] = learning_rate / 100.0
        for batch_idx, (X_train_batch,
                        Y_train_batch) in enumerate(trainloader):

            if Y_train_batch.shape[0] < batch_size:
                continue

            X_train_batch = Variable(X_train_batch).cuda()
            Y_train_batch = Variable(Y_train_batch).cuda()
            _, output = model(X_train_batch)

            loss = criterion(output, Y_train_batch)
            optimizer.zero_grad()

            loss.backward()
            optimizer.step()

    torch.save(model, 'cifar10.model')


def train_D_With_G():
    aD = Discriminator()
    aD.cuda()

    aG = Generator()
    aG.cuda()

    optimizer_g = torch.optim.Adam(aG.parameters(), lr=0.0001, betas=(0, 0.9))
    optimizer_d = torch.optim.Adam(aD.parameters(), lr=0.0001, betas=(0, 0.9))

    criterion = nn.CrossEntropyLoss()

    n_z = 100
    n_classes = 10
    np.random.seed(352)
    label = np.asarray(list(range(10)) * 10)
    noise = np.random.normal(0, 1, (100, n_z))
    label_onehot = np.zeros((100, n_classes))
    label_onehot[np.arange(100), label] = 1
    noise[np.arange(100), :n_classes] = label_onehot[np.arange(100)]
    noise = noise.astype(np.float32)

    save_noise = torch.from_numpy(noise)
    save_noise = Variable(save_noise).cuda()
    start_time = time.time()

    # Train the model
    num_epochs = 500
    loss1 = []
    loss2 = []
    loss3 = []
    loss4 = []
    loss5 = []
    acc1 = []
    for epoch in range(0, num_epochs):

        aG.train()
        aD.train()
        avoidOverflow(optimizer_d)
        avoidOverflow(optimizer_g)
        for batch_idx, (X_train_batch,
                        Y_train_batch) in enumerate(trainloader):

            if (Y_train_batch.shape[0] < batch_size):
                continue
            # train G
            if batch_idx % gen_train == 0:
                for p in aD.parameters():
                    p.requires_grad_(False)

                aG.zero_grad()

                label = np.random.randint(0, n_classes, batch_size)
                noise = np.random.normal(0, 1, (batch_size, n_z))
                label_onehot = np.zeros((batch_size, n_classes))
                label_onehot[np.arange(batch_size), label] = 1
                noise[np.arange(batch_size), :n_classes] = label_onehot[
                    np.arange(batch_size)]
                noise = noise.astype(np.float32)
                noise = torch.from_numpy(noise)
                noise = Variable(noise).cuda()
                fake_label = Variable(torch.from_numpy(label)).cuda()

                fake_data = aG(noise)
                gen_source, gen_class = aD(fake_data)

                gen_source = gen_source.mean()
                gen_class = criterion(gen_class, fake_label)

                gen_cost = -gen_source + gen_class
                gen_cost.backward()

                optimizer_g.step()

            # train D
            for p in aD.parameters():
                p.requires_grad_(True)

            aD.zero_grad()

            # train discriminator with input from generator
            label = np.random.randint(0, n_classes, batch_size)
            noise = np.random.normal(0, 1, (batch_size, n_z))
            label_onehot = np.zeros((batch_size, n_classes))
            label_onehot[np.arange(batch_size), label] = 1
            noise[np.arange(batch_size), :n_classes] = label_onehot[np.arange(
                batch_size)]
            noise = noise.astype(np.float32)
            noise = torch.from_numpy(noise)
            noise = Variable(noise).cuda()
            fake_label = Variable(torch.from_numpy(label)).cuda()
            with torch.no_grad():
                fake_data = aG(noise)

            disc_fake_source, disc_fake_class = aD(fake_data)

            disc_fake_source = disc_fake_source.mean()
            disc_fake_class = criterion(disc_fake_class, fake_label)

            # train discriminator with input from the discriminator
            real_data = Variable(X_train_batch).cuda()
            real_label = Variable(Y_train_batch).cuda()

            disc_real_source, disc_real_class = aD(real_data)

            prediction = disc_real_class.data.max(1)[1]
            accuracy = (float(prediction.eq(real_label.data).sum()) /
                        float(batch_size)) * 100.0

            disc_real_source = disc_real_source.mean()
            disc_real_class = criterion(disc_real_class, real_label)

            gradient_penalty = calc_gradient_penalty(aD, real_data, fake_data)

            disc_cost = disc_fake_source - disc_real_source + disc_real_class + disc_fake_class + gradient_penalty
            disc_cost.backward()

            optimizer_d.step()
            loss1.append(gradient_penalty.item())
            loss2.append(disc_fake_source.item())
            loss3.append(disc_real_source.item())
            loss4.append(disc_real_class.item())
            loss5.append(disc_fake_class.item())
            acc1.append(accuracy)
            if batch_idx % 50 == 0:
                print(epoch, batch_idx, "%.2f" % np.mean(loss1),
                      "%.2f" % np.mean(loss2), "%.2f" % np.mean(loss3),
                      "%.2f" % np.mean(loss4), "%.2f" % np.mean(loss5),
                      "%.2f" % np.mean(acc1))
        # Test the model
        aD.eval()
        with torch.no_grad():
            test_accu = []
            for batch_idx, (X_test_batch,
                            Y_test_batch) in enumerate(testloader):
                X_test_batch, Y_test_batch = Variable(
                    X_test_batch).cuda(), Variable(Y_test_batch).cuda()

                with torch.no_grad():
                    _, output = aD(X_test_batch)

                prediction = output.data.max(1)[
                    1]  # first column has actual prob.
                accuracy = (float(prediction.eq(Y_test_batch.data).sum()) /
                            float(batch_size)) * 100.0
                test_accu.append(accuracy)
                accuracy_test = np.mean(test_accu)
        print('Testing', accuracy_test, time.time() - start_time)

        # save output
        with torch.no_grad():
            aG.eval()
            samples = aG(save_noise)
            samples = samples.data.cpu().numpy()
            samples += 1.0
            samples /= 2.0
            samples = samples.transpose(0, 2, 3, 1)
            aG.train()
        fig = plot(samples)
        plt.savefig('output/%s.png' % str(epoch).zfill(3), bbox_inches='tight')
        plt.close(fig)

        if (epoch + 1) % 1 == 0:
            torch.save(aG, 'tempG.model')
            torch.save(aD, 'tempD.model')

    torch.save(aG, 'generator.model')
    torch.save(aD, 'discriminator.model')


# main function
train_D_Without_G()
train_D_With_G()

transform_test = transforms.Compose([
    transforms.CenterCrop(32),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

testset = torchvision.datasets.CIFAR10(root='./',
                                       train=False,
                                       download=True,
                                       transform=transform_test)
testloader = torch.utils.data.DataLoader(testset,
                                         batch_size=batch_size,
                                         shuffle=False,
                                         num_workers=8)
testloader = enumerate(testloader)

model = torch.load('cifar10.model')
model.cuda()
model.eval()
batch_idx, (X_batch, Y_batch) = testloader.__next__()
X_batch = Variable(X_batch, requires_grad=True).cuda()
Y_batch_alternate = (Y_batch + 1) % 10
Y_batch_alternate = Variable(Y_batch_alternate).cuda()
Y_batch = Variable(Y_batch).cuda()
## save real images
samples = X_batch.data.cpu().numpy()
samples += 1.0
samples /= 2.0
samples = samples.transpose(0, 2, 3, 1)

fig = plot(samples[0:100])
plt.savefig('visualization/real_images.png', bbox_inches='tight')
plt.close(fig)
_, output = model(X_batch)
prediction = output.data.max(1)[1]  # first column has actual prob.
accuracy = (float(prediction.eq(Y_batch.data).sum()) /
            float(batch_size)) * 100.0
print(accuracy)
## slightly jitter all input images
criterion = nn.CrossEntropyLoss(reduce=False)
loss = criterion(output, Y_batch_alternate)

gradients = torch.autograd.grad(outputs=loss,
                                inputs=X_batch,
                                grad_outputs=torch.ones(loss.size()).cuda(),
                                create_graph=True,
                                retain_graph=False,
                                only_inputs=True)[0]

# save gradient jitter
gradient_image = gradients.data.cpu().numpy()
gradient_image = (gradient_image - np.min(gradient_image)) / (
    np.max(gradient_image) - np.min(gradient_image))
gradient_image = gradient_image.transpose(0, 2, 3, 1)
fig = plot(gradient_image[0:100])
plt.savefig('visualization/gradient_image.png', bbox_inches='tight')
plt.close(fig)
# jitter input image
gradients[gradients > 0.0] = 1.0
gradients[gradients < 0.0] = -1.0

gain = 8.0
X_batch_modified = X_batch - gain * 0.007843137 * gradients
X_batch_modified[X_batch_modified > 1.0] = 1.0
X_batch_modified[X_batch_modified < -1.0] = -1.0

## evaluate new fake images
_, output = model(X_batch_modified)
prediction = output.data.max(1)[1]  # first column has actual prob.
accuracy = (float(prediction.eq(Y_batch.data).sum()) /
            float(batch_size)) * 100.0
print(accuracy)

## save fake images
samples = X_batch_modified.data.cpu().numpy()
samples += 1.0
samples /= 2.0
samples = samples.transpose(0, 2, 3, 1)

fig = plot(samples[0:100])
plt.savefig('visualization/jittered_images.png', bbox_inches='tight')
plt.close(fig)

lr = 0.1
weight_decay = 0.001

X = X_batch.mean(dim=0)
X = X.repeat(batch_size, 1, 1, 1)

Y = torch.arange(batch_size).type(torch.int64)
Y = Variable(Y).cuda()

for i in range(200):
    _, output = model(X)

    loss = -output[torch.arange(10).type(torch.int64),
                   torch.arange(10).type(torch.int64)]
    gradients = torch.autograd.grad(outputs=loss,
                                    inputs=X,
                                    grad_outputs=torch.ones(
                                        loss.size()).cuda(),
                                    create_graph=True,
                                    retain_graph=False,
                                    only_inputs=True)[0]

    prediction = output.data.max(1)[1]  # first column has actual prob.
    accuracy = (float(prediction.eq(Y.data).sum()) / float(10.0)) * 100.0
    print(i, accuracy, -loss)

    X = X - lr * gradients.data - weight_decay * X.data * torch.abs(X.data)
    X[X > 1.0] = 1.0
    X[X < -1.0] = -1.0

## save new images
samples = X.data.cpu().numpy()
samples += 1.0
samples /= 2.0
samples = samples.transpose(0, 2, 3, 1)

fig = plot(samples)
plt.savefig('visualization/max_class.png', bbox_inches='tight')
plt.close(fig)

lr = 0.1
weight_decay = 0.001
for extract_features in [2,4,6,8]:
    for i in range(200):
        _, output = model(X, extract_features=extract_features)

        loss = -output[torch.arange(batch_size).type(torch.int64),
                       torch.arange(batch_size).type(torch.int64)]
        gradients = torch.autograd.grad(outputs=loss,
                                        inputs=X,
                                        grad_outputs=torch.ones(
                                            loss.size()).cuda(),
                                        create_graph=True,
                                        retain_graph=False,
                                        only_inputs=True)[0]

        prediction = output.data.max(1)[1]  # first column has actual prob.
        accuracy = (float(prediction.eq(Y.data).sum()) / float(batch_size)) * 100.0
        print(i, accuracy, -loss)

        X = X - lr * gradients.data - weight_decay * X.data * torch.abs(X.data)
        X[X > 1.0] = 1.0
        X[X < -1.0] = -1.0

## save new images
samples = X.data.cpu().numpy()
samples += 1.0
samples /= 2.0
samples = samples.transpose(0, 2, 3, 1)

fig = plot(samples[0:100])
plt.savefig('visualization/max_features.png', bbox_inches='tight')
plt.close(fig)
