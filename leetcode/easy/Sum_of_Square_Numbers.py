#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/20 14:06

@desc: https://leetcode-cn.com/problems/sum-of-square-numbers/description/

'''
import math

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        a = int(math.sqrt(c))
        if a * a == c:
            return True
        for i in range(a, int(a/2), -1):
            b = int(math.sqrt(c - i * i))
            if i * i + b * b == c:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    flag = s.judgeSquareSum(0)
    print(flag)