import numpy as np
import h5py
from random import randint


class LogisticRegression:
    def __init__(self, num_inputs, num_outputs):
        self.model = {}
        self.model['W1'] = np.random.randn(
            num_outputs, num_inputs) / np.sqrt(num_inputs)
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def forward(self, x):
        x1 = np.dot(self.model['W1'], x)
        x2 = self.softmax(x1)
        return x2

    def SGD(self, x, y, lr=0.01):
        y = y.reshape(self.num_outputs, 1)
        sft_res = self.softmax(np.dot(self.model['W1'], x))
        sft_res = sft_res.reshape(self.num_outputs, 1)
        gradient = -np.dot(y - sft_res, x.T)
        self.model['W1'] -= lr * gradient
        return gradient

    def train(self, x_train, y_train, lr=0.01, max_iters=0):
        initial_lr = lr
        for it in range(max_iters):
            if it < 500:
                # warm up
                lr += (initial_lr * 10 - initial_lr) / 500
            if it % 140000 == 0:
                # step
                lr /= 10
            index = randint(0, x_train.shape[0] - 1)
            vec_y = np.zeros(self.num_outputs)
            vec_y[y_train[index]] = 1
            self.SGD(x_train[index].reshape(self.num_inputs, 1),
                     vec_y.reshape(self.num_outputs, 1), lr)

    def test(self, x_test, y_test):
        total_correct = 0

        for n in range(len(x_test)):
            y = y_test[n]
            x = x_test[n][:]
            p = self.forward(x)
            prediction = np.argmax(p)
            if prediction == y:
                total_correct += 1

        print(total_correct / np.float(len(x_test)))


if __name__ == '__main__':
    # load MNIST data
    MNIST_data = h5py.File('MNISTdata.hdf5', 'r')
    x_train = np.float32(MNIST_data['x_train'][:])
    y_train = np.int32(np.array(MNIST_data['y_train'][:, 0]))
    x_test = np.float32(MNIST_data['x_test'][:])
    y_test = np.int32(np.array(MNIST_data['y_test'][:, 0]))
    MNIST_data.close()

    # set hyper-parameters
    max_iters = 300000
    learning_rate = 0.004

    # initializa a logistic regression model
    myModel = LogisticRegression(28 * 28, 10)

    # train
    myModel.train(x_train, y_train, lr=learning_rate, max_iters=max_iters)

    # test
    myModel.test(x_test, y_test)
