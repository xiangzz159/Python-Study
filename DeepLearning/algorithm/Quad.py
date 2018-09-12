#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/18 16:58

@desc: 二次插值法

'''

def f(x):
    return x * x

'''
:param x float  当前值
:param d float  d为x处的导数
:param a float  自定义的学习率
:return float   返回调整后的学习率
'''
def GetA_Quad(x, d, a):
    c1 = 0.3
    now = f(x)
    next = f(x - a * d)

    count = 30
    while next < now:
        a *= 2
        next = f(x - a * d)
        count -= 1
        if count == 0:
            break

    count = 50
    b = 0.0
    while next > now - c1 * a * d * d:
        b = d * a * a / (now + d * a - next)
        b /= 2
        if (b < 0):
            a /= 2
        else:
            a = b

        next = f(x - a * d)
        count -= 1
        if count == 0:
            break