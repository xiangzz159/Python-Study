#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/6 14:51

@desc: https://leetcode-cn.com/problems/first-bad-version/description/

'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 0
        end = n
        while True:
            mid = (begin + end) // 2
            if isBadVersion(mid) == False and isBadVersion(mid + 1) == True:
                return mid + 1
            elif isBadVersion(mid) == False and isBadVersion(mid + 1) == False:
                begin = mid
            elif isBadVersion(mid) == True and isBadVersion(mid + 1) == True:
                end = mid


def isBadVersion(n):
    if n <= 98:
        return False
    else:
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.firstBadVersion(200))