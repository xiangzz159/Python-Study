# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/23 9:32

@desc: https://leetcode-cn.com/problems/rotated-digits/description/

'''


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        re = 0
        for i in range(1, N + 1):
            if self.check(i):
                re += 1
        return re

    def check(self, n):
        num = n
        after_num = 0
        num_list1 = [2, 5, 6, 9]
        num_list2 = [0, 1, 8]
        z = {
            0: 0,
            1: 1,
            2: 5,
            5: 2,
            6: 9,
            8: 8,
            9: 6
        }
        for i in list(str(n)):
            a = int(i)
            if a in num_list1 + num_list2:
                after_num = after_num * 10 + z[a]
            else:
                return False
        return False if after_num == n else True


if __name__ == '__main__':
    s = Solution()
    re = s.rotatedDigits(857)
    print(re)
