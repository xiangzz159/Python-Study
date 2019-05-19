#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 11:28

@desc: https://leetcode-cn.com/problems/longest-common-prefix/

'''


class Solution:
    def longestCommonPrefix(self, strs):
        common_pref = ''
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        min_n = len(strs[0])
        for i in range(1, len(strs)):
            min_n = min(min_n, len(strs[i]))
        for i in range(min_n):
            common_s = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != common_s:
                    return common_pref
            common_pref += common_s
        return common_pref



s = Solution()
re = s.longestCommonPrefix(["dog","racecar","car"])
print(re)
