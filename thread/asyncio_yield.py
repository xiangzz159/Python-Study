#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 20:48

@desc:
啥是协程：
协程,又称微线程,纤程(并发)
协程是提高单核最大效率,必须要有阻塞才会有效果提升
比线程还要少占用
原理切换-用户层面实现的切换机制

通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，
注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定

协程和线程差异：
在实现多任务时, 线程切换从系统层面远不止保存和恢复 CPU上下文这么简单。 操作系统为了程序运行的高效性每个线程都有自己缓存Cache等等数据，
操作系统还会帮你做这些数据的恢复操作。 所以线程的 切换非常耗性能。但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住
'''

import time

# yield
# 挂起当前执行的代码
# 恢复代码继续执行

def a():
    i = 0
    while i < 1000:
        print('a中', i)
        i += 1
        yield   # 等待切换到另一个yield
        time.sleep(1)

def b():
    i = 0
    while i < 1000:
        print('b中', i)
        i += 1
        yield  # 等待切换到另一个yield
        time.sleep(1)


if __name__ == '__main__':
    a1 = a()
    b1 = b()
    while True:
        next(a1)
        next(b1)