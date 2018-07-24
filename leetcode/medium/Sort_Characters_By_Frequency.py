#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/24 14:37

@desc: https://leetcode-cn.com/problems/sort-characters-by-frequency/description/

'''

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        re = ''
        s_list = list(s)
        l = [[0,0] for i in range(200)]
        for str in s_list:
            l[ord(str)][0] += 1
            l[ord(str)][1] = ord(str)
        l.sort(reverse=True)
        for i in range(len(l)):
            if l[i][0] > 0:
                re += chr(l[i][1]) * l[i][0]
        return re



if __name__ == '__main__':
    s = Solution()
    re = s.frequencySort('Aasdjklajkdsada')
    print(re)