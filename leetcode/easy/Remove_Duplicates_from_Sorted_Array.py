#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/1 13:19

@desc: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/

'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        index = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if num != nums[i]:
                num = nums[i]
                nums[index] = num
                index += 1
        return index

if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([])