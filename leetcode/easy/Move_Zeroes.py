# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/2/5 13:35

@desc: 283.Move Zeroes

'''

import math

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums


if __name__ == '__main__':
    # [0, 0, 0, 0, 1, 3, 5, 7, 12]
    nums = [0, 1, 0, 3, 12, 5, 0, 0, 7]
    solution = Solution()
    nums = solution.moveZeroes(nums)
    print(nums)