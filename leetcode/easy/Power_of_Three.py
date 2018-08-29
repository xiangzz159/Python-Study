#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/29 13:32

@desc: https://leetcode-cn.com/problems/power-of-three/description/

'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(10000):
            if 3 ** i == n:
                return True
            elif 3 ** i > n:
                return False
    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 3:
            if n == 1:
                return True
            else:
                return False
        while n > 1:
            n_ = int(n / 3)
            if n_ * 3 == n:
                n = n_
            else:
                return False
        return True

s = Solution()
print(s.isPowerOfThree2(3))