# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time : 2019/5/8 10:49

@desc: https://leetcode-cn.com/problems/validate-binary-search-tree/

中序遍历递增
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.vals = []

    def add_val(self, root):
        if root is None:
            return None
        self.add_val(root.left)
        self.vals.append(root.val)
        self.add_val(root.right)
        return self.vals

    def isValidBST(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        self.vals = self.add_val(root)
        for i in range(1, len(self.vals)):
            if self.vals[i] <= self.vals[i - 1]:
                return False
        return True

node = TreeNode(1)
l = None
r = TreeNode(1)
node.left = l
node.right = r
s = Solution()
print(s.isValidBST(node))
