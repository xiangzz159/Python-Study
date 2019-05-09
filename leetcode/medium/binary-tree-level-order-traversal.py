#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2019/5/9 10:28

@desc: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        result, q = [], [root]
        while any(q):
            tmp = []
            q_len = len(q)
            for _ in range(q_len):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(tmp)
        return result

