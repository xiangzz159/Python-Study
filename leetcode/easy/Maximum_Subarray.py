#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/2 14:19

@desc: https://leetcode-cn.com/problems/maximum-subarray/description/

'''

class Solution(object):
    def maxSubArray1(self, nums):
        """
        动态规划
        :type nums: List[int]
        :rtype: int
        """
        max_num = -1 << 32
        ans = 0
        for i in range(len(nums)):
            if ans < 0:
                ans = 0
            ans += nums[i]
            max_num = max(max_num, ans)
        return max_num

    def maxSubArray2(self, nums):
        """
        分治法
        :type nums: List[int]
        :rtype: int
        """
        return self.divide(nums, 0, len(nums) - 1)

    def divide(self, nums, left, right):
        if left == right:
            return nums[left]
        if left == right - 1:
            return max(nums[left], nums[right], nums[left] + nums[right])
        mid = (left + right) >> 1
        lret = self.divide(nums, left, mid - 1)
        rret = self.divide(nums, mid + 1, right)
        mret = nums[mid]
        total = mret
        for i in range(mid - 1, 1, -1):
            total += nums[i]
            mret = max(mret, total)

        total = mret
        for i in range(mid + 1, right):
            total += nums[i]
            mret = max(total, mret)

        return max(lret, rret, mret)





if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))