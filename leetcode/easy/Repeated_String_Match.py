#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/3 14:09

@desc: https://leetcode-cn.com/problems/repeated-string-match/description/

'''

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        count = 0
        str = ''
        bl = len(B)
        while len(str) < bl:
            count += 1
            str = A * count
        if B in str:
            return count
        count += 1
        str = A * count
        for i in range(len(str) - bl):
            if B == str[i: i + bl]:
                return count
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.repeatedStringMatch('abcd', 'cdabcdab'))