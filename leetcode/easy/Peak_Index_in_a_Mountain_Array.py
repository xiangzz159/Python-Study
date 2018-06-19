#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/19 15:24

@desc: https://leetcode-cn.com/contest/weekly-contest-89/problems/peak-index-in-a-mountain-array/

'''

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype:
        """
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                return i
        return len(A) - 1


if __name__ == '__main__':
    # t1 = time.time()
    s = Solution()
    str = s.peakIndexInMountainArray([0,1,0,0,0,0])
    print(str)
    # print(time.time() - t1)


