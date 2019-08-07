import torch
import torch.nn as nn
import torch.nn.functional as F


class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            self.convUnit(3, 196, 3, 1, 1, 1),
            self.convUnit(196, 196, 3, 1, 2, 2),
            self.convUnit(196, 196, 3, 1, 1, 3),
            self.convUnit(196, 196, 3, 1, 2, 4),
            self.convUnit(196, 196, 3, 1, 1, 5),
            self.convUnit(196, 196, 3, 1, 1, 6),
            self.convUnit(196, 196, 3, 1, 1, 7),
            self.convUnit(196, 196, 3, 1, 2, 8),
        )
        self.pool = nn.MaxPool2d(4, 4)
        self.fc1 = nn.Linear(196, 1)
        self.fc10 = nn.Linear(196, 10)

    def convUnit(self, in_c, out_c, kernel, padding, stride, conv_id):
        conv = nn.Conv2d(in_c, out_c, kernel, stride=stride, padding=padding)
        size_list = [out_c]
        if conv_id is 1:
            width_height = [32, 32]
        elif conv_id in [2, 3]:
            width_height = [16, 16]
        elif conv_id in [4, 5, 6, 7]:
            width_height = [8, 8]
        elif conv_id is 8:
            width_height = [4, 4]
        else:
            assert False, 'Invalid Conv ID!'
        size_list += width_height
        layer_norm = nn.LayerNorm(size_list)
        leaky_relu = nn.LeakyReLU(inplace=True)
        return nn.Sequential(
            conv,
            layer_norm,
            leaky_relu,
        )

    def forward(self, x, extract_features=0):
        x = self.model(x)
        h = x
        if (extract_features == 4):
            h = F.max_pool2d(h, 4, 4)
            h = h.view(-1, 196 * 4 * 4)
            return h
        elif (extract_features == 8):
            h = F.max_pool2d(h, 4, 4)
            h = h.view(-1, 196)
            return h

        x = self.pool(x)
        x = x.view(-1, 196)
        img_score = self.fc1(x)
        cls_label = self.fc10(x)
        return img_score, cls_label
