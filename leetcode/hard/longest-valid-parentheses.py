#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 13:29

@desc: https://leetcode-cn.com/problems/longest-valid-parentheses/

'''


class Solution:
    def longestValidParentheses(self, s):
        st, b = [], [0] * len(s)
        for i, val in enumerate(s):
            if val == '(':
                st.append(i)
            elif st:
                b[st.pop()], b[i] = 1, 1

        c, mc = 0, 0
        for i in b:
            if i:
                c += 1
            else:
                mc = max(c, mc)
                c = 0
        return max(c, mc)



s = Solution()
print(s.longestValidParentheses('(())()'))


