#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/23 9:12

@desc: https://leetcode-cn.com/problems/custom-sort-string/description/

'''

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        re = ''
        l = [0] * 26
        for ch in list(T):
            n = ord(ch) - ord('a')
            l[n] += 1
        for ch in list(S):
            n = l[ord(ch) - ord('a')]
            re += ch * n
            l[ord(ch) - ord('a')] = 0
        for i in range(26):
            if l[i] > 0:
                re += l[i] * chr(ord('a') + i)
        return re



if __name__ == '__main__':
    s = Solution()
    re = s.customSortString('cba', 'abcd')
    print(re)
