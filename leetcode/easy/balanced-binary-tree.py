#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/9 10:52

@desc: https://leetcode-cn.com/problems/balanced-binary-tree/

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root):
        if root is None:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

