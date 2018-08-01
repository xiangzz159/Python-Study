#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/1 13:45

@desc: https://leetcode-cn.com/problems/sort-colors/description/

'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        begin = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                self.swap(nums, begin, i)
                begin += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(nums, i, end)
                end -= 1

    def swap(self, nums, begin, end):
        num = nums[begin]
        nums[begin] = nums[end]
        nums[end] = num


if __name__ == '__main__':
    s = Solution()
    s.sortColors([0,0,2,1,1,0,2,1,2,0,0,1,1,2,1,2,0,1])
