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


def insert_sort(l):
    n = len(l)
    for i in range(1, n):
        a, b = i, i
        num = l[i]
        while num < l[a - 1] and a - 1 >= 0:
            a -= 1
            if a - 1 < 0:
                a = 0
        while b > a:
            l[b] = l[b - 1]
            b -= 1
        l[a] = num


l = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
insert_sort(l)
print(l)
