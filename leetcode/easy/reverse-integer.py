# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 10:39

@desc: https://leetcode-cn.com/problems/reverse-integer/

'''


class Solution:
    def reverse(self, x):
        x_lst = list(str(x))
        n_lst = []
        flag1 = False
        flag2 = False
        for i in range(len(x_lst) - 1, -1, -1):
            if x_lst[i] == 0 and flag1 == False:
                continue
            if x_lst[i] == '-':
                flag2 = True
                continue
            n_lst.append(x_lst[i])
            flag1 = True
        n_str = ''.join(n_lst)
        nx = int(n_str)
        if flag2:
            nx *= -1
        if -2 ** 31 < nx < 2 ** 31 - 1:
            return nx
        return 0

    def reverse1(self, x):
        if x==0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2**31<x<2**31-1:
            return x
        return 0



s = Solution()
print(s.reverse(123))
