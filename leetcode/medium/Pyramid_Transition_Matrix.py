# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/15 10:12

@desc: https://leetcode-cn.com/problems/pyramid-transition-matrix/description/

'''


class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype:
        """
        from collections import defaultdict

        mem = defaultdict(list)
        for allow in allowed:
            mem[allow[0:2]].append(allow[2])

        dp = [[False] * 10 for i in range(20)]
        n = len(bottom)
        for i in range(n):
            dp[i][ord(bottom[i]) - ord('A')] = True

        for i in range(n, -1, 0, -1):
            ndp = [[False] * 10 for i in range(20)]
            for j in range(i):
                for l in range(7):
                    for r in range(7):
                        if (dp[j][l] and dp[j + 1][r]):
                            if str(chr(65 + l) + '' + chr(65 + r) in mem):
                                for c in mem[chr(65 + l) + '' + chr(65 + r)]:
                                    ndp[j][ord(c) - ord('A')] = True
            dp = ndp
        for i in range(7):
            if (dp[0][i]):
                return True
        return False


if __name__ == '__main__':
    # t1 = time.time()
    s = Solution()
    b = s.pyramidTransition('CBDDA',
                            ["ACC", "ACA", "AAB", "BCA", "BCB", "BAC", "BAA", "CAC", "BDA", "CAA", "CCA", "CCC", "CCB",
                             "DAD", "CCD", "DAB", "ACD", "DCA", "CAD", "CBB", "ABB", "ABC", "ABD", "BDB", "BBC", "BBA",
                             "DDA", "CDD", "CBC", "CBA", "CDA", "DBA", "ABA"])
    print(b)
