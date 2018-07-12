#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/28 22:09

@desc: 简单得全连接类

'''
import numpy as np

class FC:
    def __init__(self, in_num, out_num, lr = 0.01):
        self.in_num = in_num
        self.out_num = out_num
        self.w = np.random.randn(out_num, in_num) * 10
        self.b = np.zeros(out_num)
        self.lr = lr
        print('w={}'.format(self.w))
        print('b={}'.format(self.b))

    def _sigmoid(self, in_data):
        return 1 / (1 + np.exp(-in_data))

    def forward(self, in_data):
        self.topVal =  self._sigmoid(np.dot(self.w, in_data) + self.b)
        self.bottomVal = in_data
        return self.topVal

    def backward(self, loss):
        grad_z = loss * self.topVal * (1 - self.topVal)
        grad_w = np.dot(self.bottomVal, grad_z.T)
        grad_b = np.sum(grad_z)
        self.w -= self.lr * grad_w
        self.b -= self.lr * grad_b
        grad_x = np.dot(grad_w, grad_z)
        return grad_x