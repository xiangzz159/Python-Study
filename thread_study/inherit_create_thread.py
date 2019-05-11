#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 18:00

@desc:

'''

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            print("这是子线程_", i)
            time.sleep(1)


mt = MyThread()

mt.start()

for i in range(10):
    print("这是主线程_", i)
    time.sleep(1)