#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/11 16:50

@desc: 基数排序

'''
import copy

def get_digit(x, d):
    # 获取x这个数的d位数上的数字
    # 比如获取123的1位数，结果返回3
    a = [1, 1, 10, 100] # 本实例中的最大数是百位数，所以只要到100就可以了
    return int(((x / a[d]) % 10))


def radix_sort(l, begin, end, digit):
    radix = 10 # 基数
    i, j = 0, 0
    count = []  # 存放各个桶的数据统计个数
    bucket = [0 for i in range(end - begin + 1)]
    # 按照从低位到高位的顺序执行排序过程
    for d in range(1, digit + 1):
        # 置空各个桶的数据统计
        count = [0 for i in range(radix)]
        # 统计各个桶将要装入的数据个数
        for i in range(begin, end + 1):
            j = get_digit(l[i], d)
            count[j] += 1

        # count[i]表示第i个桶的右边界索引
        for i in range(1, radix):
            count[i] = count[i] + count[i - 1]

        # 将数据依次装入桶中
        # 这里要从右往左扫描，保证排序的稳定性
        for i in range(end, begin - 1, -1):
            j = get_digit(l[i], d)
            # 求出关键码的第k位数字
            bucket[count[j] - 1] = l[i]
            # 放入相应的桶中，count[j]-1是低j个通的右边界索引
            count[j]-=1

        j = 0
        for i in range(end + 1):
            l[i] = bucket[j]
            j += 1


def sort(l):
    radix_sort(l, 0, len(l) - 1, 3)
    return l

l = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
sort(l)
print(l)



