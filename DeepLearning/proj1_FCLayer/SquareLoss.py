#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/30 22:25

@desc:

'''
import numpy as np

class SquareLoss:   # Loss 类
    def forward(self, y, t):
        self.loss = y - t
        return np.sum(self.loss * self.loss) / self.loss.shape[1] / 2

    def backward(self):
        return self.loss

class FC:   # 全连接 类
    def __init__(self, in_num, out_num, lr = 0.1):
        self.in_num = in_num
        self.out_num = out_num
        self.w = np.random.randn(in_num, out_num)
        self.b = np.zeros((out_num, 1))
        self.lr = lr

    def _sigmoid(self, in_data):
        return 1 / (1 + np.exp(-in_data))

    def forward(self, in_data):
        self.topVal = self._sigmoid(np.dot(self.w.T, in_data) + self.b)
        self.bottomVal = in_data
        return self.topVal

    def backward(self, loss):
        residual_z = loss * self.topVal * (1 - self.topVal)
        grad_w = np.dot(self.bottomVal, residual_z.T)
        grad_d = np.sum(residual_z)
        self.w -= self.lr * grad_w
        self.b -= self.lr * grad_d
        residual_x = np.dot(self.w, residual_z)
        return residual_x

class Net:  # 连接 Loss类和全连接类
    def __init__(self, input_num=2, hidden_num=4, out_num=1, lr=0.1):
        self.fc1 = FC(input_num, hidden_num, lr)
        self.fc2 = FC(hidden_num, out_num, lr)
        self.loss = SquareLoss()

    def train(self, X, Y): # X are arranged by col
        for i in range(10000):
            # forward step
            layer1out = self.fc1.forward(X)
            layer2out = self.fc2.forward(layer1out)
            loss = self.loss.forward(layer2out, y)
            # backward step
            layer2loss = self.loss.backward()
            layer1loss = self.fc2.backward(layer2loss)
            saliency = self.fc1.backward(layer1loss)
        layer1out = self.fc1.forward(X)
        layer2out = self.fc2.forward(layer1out)
        print('X = {0}'.format(X))
        print('t = {0}'.format(Y))
        print('y = {0}'.format(layer2out))


if __name__ == '__main__':
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).T
    y = np.array([[0], [0], [0], [1]]).T

    net = Net(2, 4, 1, 0.1)
    net.train(X, y)

