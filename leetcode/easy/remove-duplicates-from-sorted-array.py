#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 12:40

@desc: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

'''


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)

        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1
        return idx


s = Solution()
print(s.removeDuplicates([1,2,2,3,4,5,5,5,6,7]))