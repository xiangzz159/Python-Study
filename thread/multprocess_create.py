#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 19:47

@desc: 进程创建

进程是操作系统资源分配的基本单位
进程间是独立的数据空间,相当于子进程复制了一份代码出来,so不共享全局变量,但是一个进程中的多线程是共享全局变量的.
ps -aux : 查看系统中所有进程信息
ps -ef : 可以查看父级的ip(ppid)
top:动态显示进程信息
htop:动态显示进程信息,并显示系统资源使用情况
孤儿进程:父进程挂了,子进程还在运行
父进程回收子进程资源通过其init来回收,父进程挂了就由系统的init来
僵死进程:子进程退出,父进程没有回收子进程的资源.坏处:占用系统资源
但是python是高级语言,不用处理,可以自动回收,下一次再创建子进程时会复用之前的僵死进程资源,目的是为了减少资源的浪费,并且加速进程的创建


'''

import multiprocessing
import time

def func(queue):
    if not queue.empty():
        for i in range(queue.qsize()):
            print(queue.get_nowait())
            time.sleep(1)

def main():
    # 创建一个进程间通信队列
    queue = multiprocessing.Queue(3)

    # 申明子进程变量
    pro = multiprocessing.Process(target=func, args=(queue,))
    pro.start()

    for i in range(3):
        queue.put_nowait("消息%d" % i)

    if not queue.full():
        queue.put_nowait("消息4")
    else:
        print("消息队列满了")

    pro.join()
    pro.terminate() # 杀死进程
    time.sleep(1)
    a = pro.is_alive()  # 判断进程是否还活着，有一定延迟
    print(a)

if __name__ == '__main__':
    main()