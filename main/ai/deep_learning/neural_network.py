import numpy as np
import h5py
from random import randint


class NeuralNetwork:
    # A single hidden layer neural network
    def __init__(self, in_dim, out_dim, hidden_dim):
        model = {}
        model['W'] = np.random.randn(
            hidden_dim, in_dim) / np.sqrt(in_dim)
        model['C'] = np.random.randn(
            out_dim, hidden_dim) / np.sqrt(hidden_dim)
        model['b1'] = np.zeros(hidden_dim).reshape(hidden_dim, 1)
        model['b2'] = np.zeros(out_dim).reshape(out_dim, 1)
        self.model = model
        self.in_dimension = in_dim
        self.out_dimension = out_dim
        self.hidden_dimension = hidden_dim

    def __softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def forward(self, x):
        z = np.matmul(self.model['W'], x) + self.model['b1']
        h = self.__relu(z)
        u = np.matmul(self.model['C'], h) + self.model['b2']
        return self.__softmax(u)

    def train(self, x_train, y_train, lr, max_iters, lr_scheduler=None):
        init_lr = lr
        for it in range(max_iters):
            if lr_scheduler is not None:
                if it < lr_scheduler['warm_up']:
                    lr += (10 * init_lr - init_lr) / lr_scheduler['warm_up']

                if it % lr_scheduler['decay_step'] == 0:
                    lr /= 10

            index = randint(0, x_train.shape[0] - 1)
            vec_y = np.zeros(self.out_dimension)
            vec_y[y_train[index]] = 1
            self.__SGD(x_train[index], vec_y, lr)

    def test(self, x_test, y_test):
        total_correct = 0

        for n in range(len(x_test)):
            y = y_test[n]
            x = x_test[n][:].reshape(self.in_dimension, 1)
            p = self.forward(x)
            prediction = np.argmax(p)
            if prediction == y:
                total_correct += 1

        print(total_correct / np.float(len(x_test)))

    def __relu(self, x):
        return np.maximum(x, 0)

    def __d_relu(self, x):
        x[x >= 0] = 1
        x[x < 0] = 0
        return x

    def __SGD(self, x, y, lr):
        y = y.reshape(self.out_dimension, 1)
        x = x.reshape(self.in_dimension, 1)

        z = np.matmul(self.model['W'], x) + self.model['b1']
        h = self.__relu(z)
        u = np.matmul(self.model['C'], h) + self.model['b2']
        out = self.__softmax(u)

        drho_du = -(y - out)
        delta = np.matmul(self.model['C'].T, drho_du)

        grad_C = np.matmul(drho_du, h.T)
        grad_b2 = drho_du
        grad_b1 = delta * self.__d_relu(z)
        grad_W = np.matmul(grad_b1, x.T)

        self.model['C'] -= grad_C * lr
        self.model['W'] -= grad_W * lr
        self.model['b1'] -= grad_b1 * lr
        self.model['b2'] -= grad_b2 * lr


if __name__ == '__main__':
    # load MNIST data
    MNIST_data = h5py.File('MNISTdata.hdf5', 'r')
    x_train = np.float32(MNIST_data['x_train'][:])
    y_train = np.int32(np.array(MNIST_data['y_train'][:, 0]))
    x_test = np.float32(MNIST_data['x_test'][:])
    y_test = np.int32(np.array(MNIST_data['y_test'][:, 0]))
    MNIST_data.close()

    # set hyper-parameters
    max_iters = 180000
    learning_rate = 0.001
    num_hidden = 80
    lr_scheduler = {
        'warm_up': 500,  # lr increases linearly to 10*initial lr in 500 iters
        'decay_step': 120000  # lr divided by 10 every 110000 iters
    }

    # initializa a logistic regression model
    myModel = NeuralNetwork(28 * 28, 10, num_hidden)

    # train
    myModel.train(x_train, y_train, learning_rate,
                  max_iters, lr_scheduler)

    # test
    myModel.test(x_test, y_test)
