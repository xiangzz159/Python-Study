# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time : 2019/5/8 16:03

@desc: https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        q, result = [root], []
        while any(q):
            tmp = list()
            len_q = len(q)
            for _ in range(len_q):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.insert(0, tmp)
        return result



