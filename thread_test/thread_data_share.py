#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 18:16

@desc: 多线城间数据共享,导致数据竞争

'''

import threading
import time

g_number = 0

def hello():
    for i in range(1000000):
        global g_number
        g_number += 1

def world():
    for i in range(1000000):
        global g_number
        g_number += 1

if __name__ == '__main__':
    hello_thd = threading.Thread(target=hello)
    world_thd = threading.Thread(target=world)

    hello_thd.start()
    world_thd.start()

    # 阻塞等待
    hello_thd.join()
    world_thd.join()

    print(g_number) # 结果随机，可能小于2000000
    # 小总结: 多线程的执行顺序是随机的
    # 假设某个时间点g_number = 1000.
    # 线程1 对g_number所指向的内存地址中的数字(1000)加1;
    # 在这个时间点上,线程2也访问到g_number所指向的内存地址中的数字(1000),然在加1;
    # 这个情况下,g_number实际上只被加1