#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/25 15:14

@desc: https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/

'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level, direction = [], [root], 1
        while level:
            res.append([n.val for n in level][::direction])
            direction *= -1
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res


if __name__ == '__main__':
    node = TreeNode(3)
    l = TreeNode(9)
    r = TreeNode(20)
    rl = TreeNode(15)
    rr = TreeNode(7)
    node.left = l
    node.right = r
    node.right.left = rl
    node.right.right = rr
    s = Solution()
    print(s.zigzagLevelOrder(node))

