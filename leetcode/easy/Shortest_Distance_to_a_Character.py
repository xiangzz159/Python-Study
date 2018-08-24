#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/24 14:32

@desc:

'''

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s_l = len(S)
        if s_l == 0:
            return []

        begin = 0
        c = []
        s_ = [0 for i in range(s_l)]
        for i in range(s_l):
            if S[i] == C:
                if len(c) == 0:
                    c.append(i)
                c.append(i)
        c.append(0)
        for i in range(s_l):
            n1 = abs(c[begin] - i)
            n2 = abs(c[begin + 1] - i)
            n = min(n1, n2)
            if n == 0:
                begin += 1
                continue
            else:
                s_[i] = n
        return s_

if __name__ == '__main__':
    s = Solution()
    re = s.shortestToChar('loveleetcode', 'v')
    print(re)

