# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 11:15

@desc: https://leetcode-cn.com/problems/roman-to-integer/

'''


class Solution:
    def romanToInt(self, s):
        dic_ = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        n = len(s)
        num = 0
        i = 0
        while i < n:
            if s[i:i + 2] in dic_:
                num += dic_[s[i:i + 2]]
                i += 2
            elif s[i:i + 1] in dic_:
                num += dic_[s[i:i + 1]]
                i += 1
        if s[i:] != '':
            num += dic_[s[i:]]
        return num


s = Solution()
print(s.romanToInt('III'))
