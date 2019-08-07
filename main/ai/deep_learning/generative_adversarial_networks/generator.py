import torch
import torch.nn as nn


class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.fc1 = nn.Linear(100, 196 * 4 * 4)
        self.model = nn.Sequential(
            self.convUnit(196, 196, 4, 1, 2, 1),
            self.convUnit(196, 196, 3, 1, 1, 2),
            self.convUnit(196, 196, 3, 1, 1, 3),
            self.convUnit(196, 196, 3, 1, 1, 4),
            self.convUnit(196, 196, 4, 1, 2, 5),
            self.convUnit(196, 196, 3, 1, 1, 6),
            self.convUnit(196, 196, 4, 1, 2, 7),
            self.convUnit(196, 196, 3, 1, 1, 8),
            nn.Tanh(),
        )

    def convUnit(self, in_c, out_c, kernel, padding, stride, conv_id):
        if conv_id in [1, 5, 7]:
            conv = nn.ConvTranspose2d(in_c, out_c, kernel, stride=stride, padding=padding)
        elif conv_id in [2, 3, 4, 6, 8]:
            conv = nn.Conv2d(in_c, out_c, kernel, stride=stride, padding=padding)
            if conv_id == 8:
                return conv
        else:
            assert False, 'Invalid Conv ID!'
        batch_norm = nn.BatchNorm2d(out_c)
        relu = nn.ReLU(inplace=True)
        return nn.Sequential(
            conv,
            batch_norm,
            relu,
        )

    def forward(self, x):
        x = self.fc1(x)
        x = x.view(-1, 4, 4, 196)
        x = self.model(x)
        return x
