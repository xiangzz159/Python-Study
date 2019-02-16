#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/13 11:21

@desc:

run_until_complete 是一个阻塞（blocking）调用，直到协程运行结束，它才返回。这一点从函数名不难看出。
run_until_complete 的参数是一个 future，但是我们这里传给它的却是协程对象，之所以能这样，是因为它在内部做了检查，通过 ensure_future 函数把协程对象包装（wrap）成了 future

'''

import asyncio

async def func(x):
    print("Waitting", x, 'seconds')
    await asyncio.sleep(x)

# 回调
def done_callback(futu):
    print('Done')

futu = asyncio.ensure_future(func(3))
futu.add_done_callback(done_callback)

loop = asyncio.get_event_loop()
loop.run_until_complete(futu)