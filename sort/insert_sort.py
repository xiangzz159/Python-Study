# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/11 20:25

@desc: 快速插入排序 https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247483717&idx=1&sn=e664077a8546aff50565ab30e6979c39&scene=21#wechat_redirect

时间复杂度：O(N^2)
空间复杂度：0
稳定算法

'''


def insert_sort(arr):
    length = len(arr)
    for i in range(1, length):
        x = arr[i]
        for j in range(i, -1, -1):
            # j为当前位置，试探j-1位置
            if x < arr[j - 1]:
                arr[j] = arr[j - 1]
            else:
                # 位置确定为j
                break
        arr[j] = x


l = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
insert_sort(l)
print(l)
