# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/30 17:48

@desc: https://leetcode-cn.com/problems/implement-strstr/description/

'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hl = len(haystack)
        nl = len(needle)
        for i in range(hl - nl + 1):
            if haystack[i : i + nl] == needle:
                return i
        return -1



if __name__ == '__main__':
    s = Solution()
    print(s.strStr('', ''))
