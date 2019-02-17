#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/13 13:40

@desc:

'''

import asyncio
import time

async def func(x):
    print("Waitting", x, 'seconds')
    await asyncio.sleep(x)

def done_callback(futu):
    print('Done')

begin = int(time.time())

loop = asyncio.get_event_loop()

# 1
# futu = asyncio.ensure_future(asyncio.gather(func(1), func(2)))
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)

# 2
l = [func(1), func(2)]
futu = asyncio.ensure_future(asyncio.gather(*l))
futu.add_done_callback(done_callback)
loop.run_until_complete(futu)
print(int(time.time()) - begin)