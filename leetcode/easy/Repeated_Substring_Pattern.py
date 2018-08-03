#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/3 15:28

@desc: https://leetcode-cn.com/problems/repeated-substring-pattern/description/

'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_l = len(s)
        for i in range(int(len(s) / 2)):
            if s_l % (i + 1) == 0:
                str = s[0:i + 1]
                l = i + 1
                count = int(s_l / l)
                if str * count == s:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern(''))