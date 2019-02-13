#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 19:26

@desc: 给线城加锁，解决数据竞争

lock.acquire(True,10)
参数1：是否阻塞等待
参数2：-1表示一直阻塞，10表示10秒后解除锁不继续阻塞

'''

import threading

g_number = 0

def hello(lock):
    for i in range(10000000):
        global  g_number
        # 申请加锁
        lock.acquire()
        g_number += 1
        # 释放锁
        # print("hello")
        lock.release()

def world(lock):
    for i in range(10000000):
        global  g_number
        lock.acquire()
        g_number += 1
        # print("world")
        lock.release()


if __name__ == '__main__':
    # 申请一个锁
    lock = threading.Lock()

    hello_thd = threading.Thread(target=hello, args=(lock,))
    world_thd = threading.Thread(target=world, args=(lock,))

    hello_thd.start()
    world_thd.start()

    hello_thd.join()
    world_thd.join()

    print(g_number)
