#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/7 14:04

@desc: https://leetcode-cn.com/problems/rotate-array/description/

'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return None

        l = len(nums)
        nums = nums[l - k : l] + nums[0 : l - k]

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return None

        l = len(nums)
        for i in range(k):
            num = nums[l - 1]
            for j in range(l - 1, -1, -1):
                if j == 0:
                    nums[j] = num
                else:
                    nums[j] = nums[j - 1]

    def rotate2(self, nums, k):
        """ 三步反转法
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        if k == 0:
            return None
        self.reverseString(nums, 0, l - k - 1)
        self.reverseString(nums, l - k, l - 1)
        self.reverseString(nums, 0, l - 1)
        print(nums)

    def reverseString(self, nums, begin, end):
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1



if __name__ == '__main__':
    s = Solution()
    s.rotate2([1, 2, 3, 4, 5, 6, 7], 3)