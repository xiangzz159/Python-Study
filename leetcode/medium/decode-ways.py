#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 18:14

@desc: https://leetcode-cn.com/problems/decode-ways/

'''


class Solution:
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        n = len(s)
        d1, d2 = 1, 1
        res = d1
        for i in range(1, n):
            res = 0
            if int(s[i]) > 0:
                res += d2
            tmp = int(s[i - 1]) * 10 + int(s[i])
            if tmp >= 10 and tmp <= 26:
                res += d1
            d1 = d2
            d2 = res
        return res


s = Solution()
print(s.numDecodings('10'))