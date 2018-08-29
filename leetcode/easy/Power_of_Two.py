#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/29 13:47

@desc: https://leetcode-cn.com/problems/power-of-two/description/

'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            n_ = int(n / 2)
            if n_ * 2 == n:
                n = n_
            else:
                return False
        return True

s = Solution()
print(s.isPowerOfTwo(-16))
# for i in range(17):
#     print('%d:%s' % (i, s.isPowerOfTwo(i)))
