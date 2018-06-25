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
        lists = []
        q = []
        if root is not None:
            q.append(root)
            while q != []:
                r = q.pop(0)
                if r is not None:
                    lists.append(r.val)
                q.append(r.left)
                q.append(r.right)
        else:
            return []

        re = []
        i = 0
        while i < len(lists):
            begin = i
            end = i * 2 if i * 2 < len(lists) else len(lists)
            re.append(lists[begin : end + 1])
            i = i * 2 + 1
        return re

    def zigzagLevelOrder1(self, root):
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
    print(s.zigzagLevelOrder1(node))

