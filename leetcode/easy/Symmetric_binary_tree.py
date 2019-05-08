# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time : 2019/5/8 15:36

@desc: https://leetcode-cn.com/problems/symmetric-tree/

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSym(self, left, right):
        if not left and not right:
            return True
        if not left:
            return False
        if not right:
            return False
        return (left.val == right.val) and (self.isSym(left.left, right.right)) and (self.isSym(right.left, left.right))

    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSym(root.left, root.right)





