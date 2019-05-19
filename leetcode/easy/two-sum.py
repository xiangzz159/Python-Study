#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/19 10:23

@desc: https://leetcode-cn.com/problems/two-sum/

'''


class Solution:
    # 暴力破解
    def twoSum1(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    # 字典
    def twoSum2(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], i]
            hashmap[num] = i
        return None



s = Solution()
print(s.twoSum2([2, 7, 11, 15], 9))