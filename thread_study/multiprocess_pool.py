# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/12 20:02

@desc:
进程池概论
提前创建一定数量的进程,任务数多于进程池最大进程数量时,就等待某个进程结束,来运行下个任务;重复使用这些进程
特点:
节省重复创建进程的时间以及销毁的系统开销
自动会进程池中的进程进行管理
提高了对用户需求的响应效果

工作进程 — 就是进程池中的进程
管理进程 — 就是主进程,维护进程池,也叫控制进程

'''

import multiprocessing
import time


def func(queue):
    if not queue.empty():
        for i in range(queue.qsize()):
            print(queue.get_nowait())
            time.sleep(1)


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)

    queue = multiprocessing.Manager().Queue(10)
    for i in range(10):
        queue.put_nowait("消息%d" % i)

    if not queue.full():
        queue.put_nowait("消息10")
    else:
        print("消息队列满了")

    # pool.apply(func=func, args=(queue,))        # 添加任务并阻塞等待任务执行完成，能保证顺序
    pool.apply_async(func=func, args=(queue,))  # 异步添加任务，不足赛任务执行完成

    pool.close()
    pool.join()
    print('End')
