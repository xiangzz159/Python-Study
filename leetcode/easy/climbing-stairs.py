#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/17 10:43

@desc: https://leetcode-cn.com/problems/climbing-stairs/

'''


class Solution:
    def climbStairs(self, n):
        lst = [1, 2]
        if n < 2:
            return lst[n - 1]
        for i in range(2, n):
            lst.append(lst[i - 2] + lst[i - 1])
        return lst[-1]


s = Solution()
print(s.climbStairs(1))

