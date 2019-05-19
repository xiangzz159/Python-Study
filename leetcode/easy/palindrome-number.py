#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 11:09

@desc: https://leetcode-cn.com/problems/palindrome-number/

'''


class Solution:
    def isPalindrome(self, x):
        str_x = str(x)
        n = len(str_x)
        for i in range(int(n / 2)):
            if str_x[i] != str_x[n - 1 - i]:
                return False
        return True



