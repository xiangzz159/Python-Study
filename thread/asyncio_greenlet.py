#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 20:57

@desc:

greenlet是对yield的封装
'''

from greenlet import greenlet
import time


def test1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("---B--")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)


# 切换到gr1中运行

gr1.switch()