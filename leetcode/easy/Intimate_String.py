#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/25 14:23

@desc: https://leetcode-cn.com/contest/weekly-contest-90/problems/buddy-strings/

'''

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        count = 0
        chars = {}
        char_list = []
        flag = False
        for i in range(0, len(A)):
            if A[i] != B[i]:
                count += 1
                char_list.append(A[i])
                char_list.append(B[i])
            if A[i] not in chars:
                chars[A[i]] = 0
            chars[A[i]] += 1
        for key in chars.keys():
            if chars[key] > 1:
                flag = True
                break
        char_list = set(char_list)
        return (count == 2 and len(char_list) == 2) or (count == 0 and flag)


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings('aaaaaaabc', 'aaaaaaacb'))