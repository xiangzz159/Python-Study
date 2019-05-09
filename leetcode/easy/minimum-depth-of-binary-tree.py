#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/9 11:02

@desc: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def minDepth(self, root):
        if root is None:
            return 0
        lt, rt = self.minDepth(root.left), self.minDepth(root.right)
        return 1 + min(lt, rt) if lt and rt else 1 + lt + rt

