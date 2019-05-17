#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/17 10:28

@desc:

'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            lens = max(len1, len2)
            if lens > end - start:
                start = i - int((lens - 1) / 2)
                end = i + int(lens / 2)
        return s[start:end + 1]

    def expandAroundCenter(self, s, l, r):
        L, R = l, r
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1


s = Solution()
ss = "babaddab"
print(s.longestPalindrome(ss))