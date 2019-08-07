import numpy as np
import h5py
from random import randint


class ConvNet:
    def __init__(self, in_channels, out_channels, kernel_size, num_classes, img_size):
        model = {}
        model['K'] = np.random.randn(kernel_size, kernel_size, out_channels)
        new_img_size = img_size - kernel_size + 1
        model['W'] = np.random.randn(num_classes, new_img_size, new_img_size,
                                     out_channels) / np.sqrt(new_img_size * new_img_size * out_channels)
        model['b'] = np.zeros(num_classes).reshape(num_classes, 1)

        self.model = model
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.img_size = img_size
        self.new_img_size = new_img_size
        self.num_classes = num_classes

    def convolution(self, x, k):
        z = []
        kernel_size = k.shape[1]

        img_size = x.shape[0]
        new_img_size = img_size - kernel_size + 1
        for i in range(k.shape[2]):
            kernel = k[:, :, i].reshape(kernel_size, kernel_size, -1)
            result = np.zeros(
                new_img_size ** 2).reshape(new_img_size, new_img_size)
            for j in range(new_img_size):
                for l in range(new_img_size):
                    result[j][l] = np.sum(
                        kernel * x[j:j + kernel_size, l:l + kernel_size, :])
            z.append(result)
        z = np.array(z)
        return np.transpose(z, (1, 2, 0))

    def forward(self, x):
        z = self.convolution(x, self.model['K'])
        h = self.relu(z)
        h = h.reshape(self.new_img_size * self.new_img_size *
                      self.out_channels, -1)
        u = np.matmul(self.model['W'].reshape(-1, self.new_img_size * self.new_img_size *
                                              self.out_channels), h) + self.model['b']
        pred = self.softmax(u)
        res = {}
        res['z'] = z
        res['h'] = h
        res['u'] = u
        res['pred'] = pred

        return res

    def train(self, x_train, y_train, lr, max_iters):
        print('training...')
        for it in range(max_iters):
            print(str(it))
            index = randint(0, x_train.shape[0] - 1)
            vec_y = np.zeros(self.num_classes)
            vec_y[y_train[index]] = 1
            self.SGD(x_train[index], vec_y, lr)

    def test(self, x_test, y_test):
        total_correct = 0
        print('testing...')

        for n in range(len(x_test)):
            print(n)
            y = y_test[n]
            x = x_test[n][:].reshape(
                self.img_size, self.img_size, self.in_channels)
            p = self.forward(x)['pred']
            prediction = np.argmax(p)
            if prediction == y:
                total_correct += 1

        print(total_correct / np.float(len(x_test)))

    def relu(self, x):
        return np.maximum(x, 0)

    def d_relu(self, x):
        x[x >= 0] = 1
        x[x < 0] = 0
        return x

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def SGD(self, x, y, lr):
        x = x.reshape(self.img_size, self.img_size, self.in_channels)
        y = y.reshape(self.num_classes, 1)

        res = self.forward(x)

        drho_du = -(y - res['pred'])
        grad_b = drho_du
        self.model['b'] -= lr * grad_b

        delta = np.matmul(drho_du.reshape(1, -1),
                          self.model['W'].reshape(self.num_classes, -1))

        for i in range(self.num_classes):
            drho_duk = drho_du[i]
            grad_Wk = drho_duk * res['h']
            grad_Wk = grad_Wk.reshape(self.new_img_size, self.new_img_size, -1)
            self.model['W'][i] -= lr * grad_Wk

        temp = (self.d_relu(res['z']).reshape(1, -1)) * delta
        grad_K = self.convolution(x, temp.reshape(
            self.new_img_size, self.new_img_size, self.out_channels))
        self.model['K'] -= lr * grad_K


if __name__ == '__main__':

    MNIST_data = h5py.File('MNISTdata.hdf5', 'r')
    x_train = np.float32(MNIST_data['x_train'][:])
    y_train = np.int32(np.array(MNIST_data['y_train'][:, 0]))
    x_test = np.float32(MNIST_data['x_test'][:])
    y_test = np.int32(np.array(MNIST_data['y_test'][:, 0]))
    print(len(x_test))
    MNIST_data.close()

    num_classes = 10
    kernel_size = 3
    in_channels = 1
    out_channels = 6
    img_size = 28
    learning_rate = 0.01
    max_iters = 60000

    myModel = ConvNet(in_channels, out_channels,
                      kernel_size, num_classes, img_size)

    myModel.train(x_train, y_train, learning_rate, max_iters)

    myModel.test(x_test, y_test)

    print('learning rate: %f, max iters: %d, out channels: %d' %
          (learning_rate, max_iters, out_channels))
