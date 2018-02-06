# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/2/6 10:13

@desc: 389. Find the Difference

'''

import collections

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list((collections.Counter(t) - collections.Counter(s)))[0]


if __name__ == '__main__':
    solution = Solution()
    s = 'abcd'
    t = 'abcde'
    re = solution.findTheDifference(s, t)
    print(re)
