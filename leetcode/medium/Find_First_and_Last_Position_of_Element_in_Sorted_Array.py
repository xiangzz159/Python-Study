#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/6 14:21

@desc: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        begin = 0
        end = len(nums) - 1
        while begin < end and (nums[begin] != target or nums[end] != target):
            if nums[begin] != target:
                begin += 1
            if nums[end] != target:
                end -= 1
        if nums[begin] == target and nums[end] == target:
            return [begin, end]
        else:
            return [-1, -1]




if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10],8))