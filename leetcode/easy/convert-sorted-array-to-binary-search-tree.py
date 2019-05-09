#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/9 10:35

@desc: https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        nums.sort()
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        l_list = nums[:mid]
        r_list = nums[mid + 1:]
        root.left = self.sortedArrayToBST(l_list)
        root.right = self.sortedArrayToBST(r_list)
        return root


