import os
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torchvision.datasets as datasets
import torchvision.transforms as transforms

# configuration
cfg = {
    'name': 'ex1',  # name of experiment, used to name weight folder
    'dataset': 'CIFAR10',  # name of dataset
    'image size': 32,  # image size after data augmentation
    'in channels': 3,  # original image channels
    'num classes': 10,  # number of class prediction
    'kernel size': 3,  # kernel size of each convolutional layer
    'learning rate': 0.001,  # learning rate
    'lr scheduler': [25, 35],  # learning rate scheduler to adjust lr
    'max epochs': 45,  # maximum number of epochs
    'start epoch': 0,  # starting epoch (load model and continue)
    'batch size': 16,  # batch size
    'optimizer': 'Adam',  # optimizer chosen from {Adam, RMSprop, SGD}
    'cuda': True,  # use cuda or not
    'print': True,  # print detail message or not
    'pretrained': '',  # pretrained model address, if '' then random init
    'eval': True,  # evaluation mode, only test if True
    'save path': './checkpoints/',  # path to save the weights
    'save interval': 5,  # epoch interval to save the weights
}

device = torch.device('cuda:0' if cfg['cuda']
                      and torch.cuda.is_available() else 'cpu')


class DeepConvNet(nn.Module):

    def __init__(self, image_size, in_channels=1, num_classes=2, kernel_size=3):
        super(DeepConvNet, self).__init__()

        self.img_size = image_size
        self.in_channels = in_channels
        self.num_classes = num_classes
        self.kernel_size = kernel_size

        self.feature_extractor = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=kernel_size, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, stride=2),
            nn.Conv2d(64, 128, kernel_size=kernel_size, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 256, kernel_size=kernel_size, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, stride=2),
            nn.Conv2d(256, 512, kernel_size=kernel_size, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, stride=2),
        )

        fm_size = cfg['image size']
        fm_size = (fm_size - kernel_size + 2 + 1) / 2
        fm_size = fm_size - kernel_size + 2 + 1
        fm_size = (fm_size - kernel_size + 2 + 1) / 2
        fm_size = (fm_size - kernel_size + 2 + 1) / 2
        self.feature_map_size = int(fm_size)

        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear((self.feature_map_size ** 2) * 512, 128, bias=True),
            nn.ReLU(inplace=True),
            nn.Linear(128, 64, bias=True),
            nn.ReLU(inplace=True),
            nn.Linear(64, num_classes, bias=True),
        )

    def forward(self, x):
        feature_map = self.feature_extractor(x)
        feature_map = feature_map.view(-1, (self.feature_map_size ** 2) * 512)
        output = self.classifier(feature_map)
        return output


def train(model, train_loader):
    save_path = './checkpoints/' + \
        cfg['name'] if cfg['name'] != '' else './checkpoints/default'
    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    criterion = nn.CrossEntropyLoss()
    if cfg['optimizer'] == 'Adam':
        optimizer = optim.Adam(model.parameters(), lr=cfg['learning rate'])
    elif cfg['optimizer'] == 'RMSprop':
        optimizer = optim.RMSprop(model.parameters(), lr=cfg['learning rate'])
    else:
        optimizer = optim.SGD(model.parameters(), lr=cfg['learning rate'])

    if len(cfg['lr scheduler']) > 0:
        scheduler = optim.lr_scheduler.MultiStepLR(
            optimizer, cfg['lr scheduler'])

    for epoch in range(cfg['start epoch'], cfg['max epochs']):
        scheduler.step()
        epoch_loss = 0.0
        count = 0
        for it, (x, y) in enumerate(train_loader):
            x = x.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            pred = model(x)
            loss = criterion(pred, y)
            if cfg['print']:
                print('epoch: %d | iter: %d | loss: %f' %
                      (epoch + 1, it + 1, loss.item()))
            epoch_loss += loss.item()
            count += 1
            loss.backward()
            optimizer.step()

        if cfg['print']:
            print('epoch %d ends, average loss: %f' %
                  (epoch + 1, epoch_loss / count))

        if (epoch + 1) % cfg['save interval'] == 0:
            if cfg['print']:
                print('save model weights of epoch %d to %s' %
                      (epoch + 1, cfg['save path']))
            torch.save(model.state_dict(),
                       save_path + '/epoch' + str(epoch + 1) + '.pth')
    model.eval()


def test(model, test_loader):
    num_sample = 0
    num_correct = 0
    with torch.no_grad():
        for it, (x, y) in enumerate(test_loader, 0):
            x = x.to(device)
            y = y.to(device)
            pred = model(x)
            _, ans = torch.max(pred, 1)
            num_sample += y.shape[0]
            num_correct += (ans == y).sum().item()
            if cfg['print']:
                print('test iter: %d | number of correct pred: %d' %
                      (it + 1, (ans == y).sum().item()))
    print('accuracy: %.2f/1.00' % (num_correct / num_sample))


if __name__ == '__main__':
    if cfg['print']:
        print('using device: %s' % device)
        print('creating model...')

    model = DeepConvNet(cfg['image size'], cfg['in channels'],
                        cfg['num classes'], cfg['kernel size'])

    if cfg['pretrained'] != '':
        if cfg['print']:
            print('load pretrained model from %s' % cfg['pretrained'])
        model.load_state_dict(torch.load(cfg['pretrained']))

    if cfg['eval']:
        model.eval()
    else:
        model.train()

    model = model.to(device)

    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomCrop(size=[32, 32], padding=4),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    if cfg['print']:
        print('prepare %s dataset...' % cfg['dataset'])
    train_set = datasets.CIFAR10(
        root='.', train=True, download=True, transform=transform)
    test_set = datasets.CIFAR10(
        root='.', train=False, download=False, transform=transform)

    train_loader = data.DataLoader(
        train_set, batch_size=cfg['batch size'], shuffle=True, num_workers=4)
    test_loader = data.DataLoader(
        test_set, batch_size=cfg['batch size'], shuffle=False, num_workers=4)

    if not cfg['eval']:
        if cfg['print']:
            print('start training: max epochs: %d | start epoch: %d | batch size: %d' %
                  (cfg['max epochs'], cfg['start epoch'] + 1, cfg['batch size']))
            print('learning rate %f | optimizer: %s' %
                  (cfg['learning rate'], cfg['optimizer']))
        train(model, train_loader)

    if cfg['print']:
        print('start testing:')
    test(model, test_loader)

    if cfg['print']:
        print('test finished!')
