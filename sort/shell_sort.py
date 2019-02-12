#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/11 20:26

@desc: 希尔排序 https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247483735&idx=1&sn=ce1ee1707dbc63f12130c30e6f81f24c&scene=21#wechat_redirect

'''

def shell_sort(L):
    n = len(L)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap:
                if L[j] < L[j - gap]:
                    L[j], L[j - gap] = L[j - gap], L[j]
                    j -= gap
                else:
                    break
            gap //= 2

l = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
shell_sort(l)
print(l)