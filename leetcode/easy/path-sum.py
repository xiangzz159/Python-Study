#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/9 11:15

@desc: https://leetcode-cn.com/problems/path-sum/

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum - root.val == 0
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum-root.val)
