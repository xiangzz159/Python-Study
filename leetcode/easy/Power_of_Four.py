#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/29 13:43

@desc: https://leetcode-cn.com/problems/power-of-four/description/

'''


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 4:
            if num == 1:
                return True
            else:
                return False
        while num > 1:
            num_ = int(num / 4)
            if num_ * 4 == num:
                num = num_
            else:
                return False
        return True


s = Solution()
print(s.isPowerOfFour(16))