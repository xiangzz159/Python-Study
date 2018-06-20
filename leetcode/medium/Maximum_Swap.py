# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/20 14:24

@desc: https://leetcode-cn.com/problems/maximum-swap/description/

'''
from math import pow


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = list(str(num))
        ans = A[:]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans:
                    ans = A[:]
                A[i], A[j] = A[j], A[i]

        return int("".join(ans))



if __name__ == '__main__':
    s = Solution()
    flag = s.maximumSwap(9919)
    print(flag)
