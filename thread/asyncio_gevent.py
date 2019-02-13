#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 21:01

@desc:
gevent是对greenlet的二次封装,能够自动切换任务模块

其原理是当一个greenlet遇到IO操作(指的是input output 输入输出，比如网络、文件操作等需要耗时等待的操作)时,就自动切换到其他的greenlet,等到IO操作文采,再在合适的时候切换回来继续执行

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO

'''

import gevent

from gevent import monkey
import random
import time

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


def main1():
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)

    g1.join()
    g2.join()
    g3.join()

# 取消python耗时
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的代码

def coroutine_word(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())

def main2():
    gevent.joinall([
        gevent.spawn(coroutine_word, 'work1'),
        gevent.spawn(coroutine_word, 'work2')
    ])
