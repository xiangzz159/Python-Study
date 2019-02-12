#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/11 20:25

@desc: 快速排序 https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247483714&idx=1&sn=5d352c58a48ccc96280a1333ec23c27f&scene=21#wechat_redirect

'''

def quick_sort(a, l, r):
    if l < r:
        i, j = l, r
        base = a[i]
        while i < j:
            while i < j and a[j] >= base:
                j -= 1

            a[i] = a[j]

            while i < j and a[i] <= base:
                i += 1
            a[j] = a[i]

        a[i] = base

        quick_sort(a, l, i - 1)
        quick_sort(a, j + 1, r)

l = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
quick_sort(l, 0, len(l) - 1)
print(l)