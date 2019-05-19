#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 11:41

@desc: https://leetcode-cn.com/problems/valid-parentheses/

'''


class Solution:
    def isValid(self, s):
        if s == '' or s is None:
            return True
        stock = []
        n = len(s)
        for i in range(n):
            if s[i] in ['(', '[', '{']:
                stock.append(s[i])
            elif s[i] in [')', ']', '}']:
                if len(stock) == 0:
                    return False
                x = stock.pop(-1)
                if (x == '[' and s[i] == ']') or (x == '(' and s[i] == ')') or (x == '{' and s[i] == '}'):
                    continue
                else:
                    return False
        if len(stock) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid(']'))