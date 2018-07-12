#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/12 15:02

@desc: https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/description/

'''

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            count += nums[j] - nums[i]
            j -= 1
            i += 1

        return count

if __name__ == '__main__':
    s = Solution()
    num = s.minMoves2([1, 2, 3, 4])
    print(num)