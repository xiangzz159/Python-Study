#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/29 13:57

@desc: https://leetcode-cn.com/problems/number-of-1-bits/description/

'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = int(n / 2)
        return count

s = Solution()
print(s.hammingWeight(128))


