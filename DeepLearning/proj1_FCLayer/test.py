#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/28 22:14

@desc:
https://zhuanlan.zhihu.com/p/21525237
https://blog.csdn.net/u012938704/article/details/52595839
'''

from DeepLearning.proj1_FCLayer.FC import FC
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw3D(X,Y,Z,angle=None):
    fig=plt.figure(figsize=(15,7))
    ax=Axes3D(fig)
    if angle:
        ax.view_init(angle[0],angle[1])
    ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
    plt.show()

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
X_f = X.flatten()
Y_f = Y.flatten()
data = zip(X_f, Y_f)

def test1():
    fc = FC(2, 1)
    Z1 = np.array([fc.forward(d) for d in data])
    print('Z1={0}'.format(Z1))
    Z1 = Z1.reshape((100, 100))
    print('Z1={0}'.format(Z1))
    draw3D(X, Y, Z1)

def test2():
    fc = FC(2, 3)
    fc.w = np.array([[0.4, 0.6],[0.3,0.7],[0.2,0.8]])
    fc.b = np.array([0.5, 0.5, 0.5])

    fc2 = FC(3, 1)
    fc2.w = np.array([0.3, 0.2, 0.1])
    fc2.b = np.array([0.5])

    Z1 = np.array([fc.forward(d) for d in data])
    Z2 = np.array([fc2.forward(d) for d in Z1])
    Z2 = Z2.reshape((100, 100))
    draw3D(X, Y, Z2, (40, -45))

def test3():
    fc = FC(2, 3)
    fc.w = np.array([[-0.4, 1.6], [-0.3, 0.7], [0.2, -0.8]])
    fc.b = np.array([-0.5, 0.5, 0.5])

    fc2 = FC(3,1)
    fc2.w = np.array([-3, 2, -1])
    fc2.b = np.array([0.5])

    Z1 = np.array([fc.forward(d) for d in data])
    Z2 = np.array([fc2.forward(d) for d in Z1])
    Z2 = Z2.reshape(100, 100)

    draw3D(X, Y, Z2)

if __name__ == '__main__':
    # test1()
    x = [i for i in range(1, 4)]
    y = [i for i in range(10, 18)]
    X, Y = np.meshgrid(x, y)
    print('X={0}'.format(X))
    print('X_F={}'.format(X.flatten()))
    print('Y={0}'.format(Y))
    print('Y_F={}'.format(Y.flatten()))
    data = zip(X_f, Y_f)
    print('zip(X_f, Y_f)={}'.format(data))
