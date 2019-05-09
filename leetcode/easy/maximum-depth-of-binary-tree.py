#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/9 10:09

@desc: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
