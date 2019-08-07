import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import torch.utils.model_zoo as model_zoo
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torchvision.models as models


cfg = {
    'name': 'ex2',
    'dataset_path': '/projects/training/bawc/CIFAR100/Dataset/',
    'layers': [2, 4, 4, 2],
    'img_size': 32,
    'num_classes': 100,
    'lr': 0.001,
    'batch_size': 16,
    'start_epoch': 0,
    'max_epochs': 50,
    'optimizer': 'Adam',
    'pretrained': './checkpoints/ex2/epoch15.pth',
    'eval': True,
    'use_classical': False,
    'cuda': True,
    'save_interval': 5,
}

model_urls = {
    'resnet18': '/projects/training/bawc/CIFAR100/Model/resnet18-5c106cde.pth'
}

device = torch.device('cuda' if cfg['cuda'] and torch.cuda.is_available() else 'cpu')


def resnet18(pretrained=True):
    model = models.resnet.ResNet(models.resnet.BasicBlock, [2, 2, 2, 2])
    if pretrained:
        model.load_state_dict(model_zoo.load_url(
            model_urls['resnet18'],
            model_dir='./checkpoints/' + cfg['name'] + '/'))
    return model


class BasicBlock(nn.Module):

    def __init__(self, in_channels, out_channels, stride=1):
        super(BasicBlock, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, stride=stride, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, 3, stride=1, padding=1),
            nn.BatchNorm2d(out_channels),
        )
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.stride = stride
        if stride > 1 or in_channels != out_channels:
            self.downsample = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 1, stride=stride),
                nn.BatchNorm2d(out_channels),
            )
        else:
            self.downsample = None

    def forward(self, x):
        identity = x
        x = selfT.layer(x)
        if self.downsample is not None:
            identity = self.downsample(identity)
        return F.relu(x + identity)


class ResNet(nn.Module):

    def __init__(self):
        super(ResNet, self).__init__()
        self.head = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.1),
        )
        self.layer1 = self.build_layer(32, 32, 1, 0)
        self.layer2 = self.build_layer(32, 64, 2, 1)
        self.layer3 = self.build_layer(64, 128, 2, 2)
        self.layer4 = self.build_layer(128, 256, 2, 3)
        self.middle = nn.Sequential(
            self.layer1,
            self.layer2,
            self.layer3,
            self.layer4,
            nn.MaxPool2d(2, 2),
        )
        self.classifier = nn.Sequential(
            nn.Linear(256 * 2 * 2, 1024),
            nn.ReLU(inplace=True),
            nn.Linear(1024, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, cfg['num_classes']),
        )

    def build_layer(self, in_channels, out_channels, stride, idx=0):
        layer = []
        for i in range(cfg['layers'][idx]):
            if i == 0:
                block = BasicBlock(in_channels, out_channels, stride=stride)
            else:
                block = BasicBlock(out_channels, out_channels)
            layer.append(block)
        return nn.Sequential(*layer)

    def forward(self, x):
        x = self.head(x)
        x = self.middle(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x


def train(model, train_loader):
    save_path = './checkpoints/' + cfg['name'] if cfg['name'] != '' else './checkpoints/default'
    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    criterion = nn.CrossEntropyLoss()
    if cfg['optimizer'] == 'Adam':
        optimizer = optim.Adam(model.parameters(), lr=cfg['lr'])
    elif cfg['optimizer'] == 'RMSprop':
        optimizer = optim.RMSprop(model.parameters(), lr=cfg['lr'])
    else:
        optimizer = optim.SGD(model.parameters(), lr=cfg['lr'])

    for epoch in range(cfg['start_epoch'], cfg['max_epochs']):
        epoch_loss = 0.0
        count = 0
        for it, (x, y) in enumerate(train_loader):
            x = x.to(device)
            y = y.to(device)
            optimizer.zero_grad()
            pred = model(x)
            loss = criterion(pred, y)
            print('epoch: %d | iter: %d | loss: %f' %
                  (epoch + 1, it + 1, loss.item()))
            epoch_loss += loss.item()
            count += 1
            loss.backward()
            optimizer.step()

        print('epoch %d ends, average loss: %f' %
              (epoch + 1, epoch_loss / count))

        if (epoch + 1) % cfg['save_interval'] == 0:
            print('save model weights of epoch %d to %s' %
                  (epoch + 1, save_path))
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
            print('test iter: %d | number of correct pred: %d' %
                  (it + 1, (ans == y).sum().item()))
    print('Accuracy: %.2f/1.00' % (num_correct / num_sample))


if __name__ == '__main__':
    print('Using device: %s' % device)
    print('Creating model...')
    model = resnet18() if cfg['use_classical'] else ResNet()
    print('Model ready!')
    if cfg['pretrained'] != '':
        print('load pretrained model from %s' % cfg['pretrained'])
        model.load_state_dict(torch.load(cfg['pretrained']))
    if cfg['eval']:
        print('Start evaluation mode...')
        model.eval()
    else:
        print('Start train mode...')
        model.train()
    print('Move the model to device...')
    model.to(device)
    trans_padding = 28 if cfg['use_classical'] else 4
    trans = [transforms.Resize(224)] if cfg['use_classical'] else []
    trans += [
        transforms.RandomHorizontalFlip(),
        transforms.RandomCrop(size=[cfg['img_size'], cfg['img_size']], padding=trans_padding),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.507, 0.487, 0.441], std=[0.267, 0.256, 0.276])
    ]
    transform = transforms.Compose(trans)
    print('Load data...')
    if not cfg['eval']:
        train_set = datasets.CIFAR100(root='.', train=True, download=True, transform=transform)
        train_loader = data.DataLoader(train_set, batch_size=cfg['batch_size'], shuffle=True, num_workers=4)
        print('Train data done!')
    test_set = datasets.CIFAR100(root='.', train=False, download=False, transform=transform)
    test_loader = data.DataLoader(test_set, batch_size=16, shuffle=False, num_workers=1)
    print('Test data done!')

    if not cfg['eval']:
        print('Start training: max epochs: %d | start epoch: %d | batch size: %d' %
              (cfg['max_epochs'], cfg['start_epoch'] + 1, cfg['batch_size']))
        print('learning rate %f | optimizer: %s' % (cfg['lr'], cfg['optimizer']))
        train(model, train_loader)
        print('Finish training!')
    print('Start testing...')
    test(model, test_loader)
    print('Finish testing!')
