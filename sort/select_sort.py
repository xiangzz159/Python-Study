#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/11 20:17

@desc: 选择排序 https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247483704&idx=1&sn=3d056587972675ba725c0ef2c2632709&scene=21#wechat_redirect

时间复杂度：O(N^2)
空间复杂度：0
稳定算法

'''

def select_sort(l):
    n = len(l)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if l[j] < l[min]:
                min = j

        if min != i:
            l[i], l[min] = l[min], l[i]

l = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
select_sort(l)
print(l)