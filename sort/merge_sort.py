#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/2/11 20:24

@desc: 归并排序 https://mp.weixin.qq.com/s?__biz=MzU2MTI4MjI0MQ==&mid=2247483773&idx=1&sn=bc7c4eed3f7ee8f7189ae149dd73a719&scene=21#wechat_redirect

时间复杂度：O(nlogn)
稳定算法

'''

def merge_sort(L):
    if len(L) <= 1:
        return L
    num = int(len(L) / 2)
    left = merge_sort(L[:num])
    right = merge_sort(L[num:])
    return merge(left, right)

def merge(left, right):
    ri, le = 0, 0
    result = []
    while le < len(left) and ri < len(right):
        if left[le] < right[ri]:
            result.append(left[le])
            le += 1
        else:
            result.append(right[ri])
            ri += 1

    result += left[le:]
    result += right[ri:]
    return result

print(merge_sort([50, 123, 543, 187, 49, 30, 0, 2, 11, 100]))