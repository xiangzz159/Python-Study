#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 17:53

@desc:

进程是资源分配的独立单位,线程是操作系统调度的基本执行单位
一个程序中默认有一个主进程,一个进程中默认有一个主线程
进程间是不共享数据,线程间是共享数据
多进程和多线程的执行顺序是无序的
程序会等待所有进程结束再关闭退出,进程结束则关闭释放资源
进程结束,此进程里的多线程会强制关闭释放资源,可以在进程中加上time.sleep来暂缓进程的结束
---------------------
作者：宁致乐水
来源：CSDN
原文：https://blog.csdn.net/qq_31603575/article/details/80223950
版权声明：本文为博主原创文章，转载请附上博文链接！

'''

import threading
import time

def sayHello(no, age = 10):
    for i in range(2):
        print("hello:", no)
        time.sleep(1)

print("Start")
for i in range(3):
    thd = threading.Thread(target=sayHello, args=(i, ), kwargs={"age": 100})
    thd.start()

while True:
    if len(threading.enumerate()) == 1:
        print("thread enumerate is 1")
        break
    else:
        time.sleep(1)

thd.join()
print("End")
