# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/17 12:23

@desc: https://leetcode-cn.com/problems/permutations/

'''


class Solution:
    def permute(self, nums):
        if nums is None:
            return []
        if len(nums) == 1:
            return [nums]
        l = []
        self.func(nums, 0, len(nums), l)
        return l

    def func(self, nums, begin, end, l):
        if begin == end:
            if tuple(nums) not in l:
                l.append(tuple(nums))
        else:
            for j in range(begin, end):
                nums[begin], nums[j] = nums[j], nums[begin]
                self.func(nums, begin + 1, end, l)
                nums[j], nums[begin] = nums[begin], nums[j]


s = Solution()
l = s.permute([1, 1, 3])
print(l)
