#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/1 13:27

@desc: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/description/

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
        num_size = 1
        for i in range(1, len(nums)):
            if (num == nums[i] and num_size % 2 != 0):
                num = nums[i]
                nums[index] = num
                index += 1
                num_size += 1
            if num != nums[i]:
                num = nums[i]
                nums[index] = num
                index += 1
                num_size = 1
        return index

if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([0,0,1,1,1,1,2,3,3])