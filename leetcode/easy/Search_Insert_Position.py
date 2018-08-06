#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/6 15:42

@desc:

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums)
        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid
        return (begin + end) // 2

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 0))