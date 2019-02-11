#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/11 18:25

@desc:  冒泡排序

'''

def bubble_sort(l):
    n = len(l)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


l = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
bubble_sort(l)
print(l)