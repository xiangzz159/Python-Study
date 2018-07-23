#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/23 10:43

@desc: https://leetcode-cn.com/problems/distinct-subsequences/description/

'''
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_length = len(s)
        t_length = len(t)
        space = [[0 for i in range(t_length + 1)] for j in range (s_length + 1)]
        for i in range(s_length + 1):
            space[i][0] = 1
        for i in range(1, s_length + 1):
            for j in range(1, t_length + 1):
                if s[i-1] == t[j-1]:
                    space[i][j] = space[i-1][j-1] + space[i-1][j]
                else:
                    space[i][j] = space[i-1][j]
        return space[s_length][t_length]

if __name__ == '__main__':
    s = Solution()
    re = s.numDistinct('rabbbit', 'rabbit')