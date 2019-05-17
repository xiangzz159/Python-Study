#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/17 10:48

@desc:

'''


class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        result = []
        result.append(nums[0])
        result.append(max(nums[0], nums[1]))

        n = len(nums)
        for i in range(2, n):
            result.append(max(result[i - 1], result[i -2] + nums[i]))
        return result[-1]




s = Solution()

print(s.rob([2, 1, 1, 2]))
