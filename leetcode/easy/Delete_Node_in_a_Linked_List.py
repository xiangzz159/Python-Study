#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/28 11:05

@desc: https://leetcode-cn.com/problems/delete-node-in-a-linked-list/description/

'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None:
            return node
        if node.next == None:
            node = None
        node.val = node.next.val
        node.next = node.next.next


s = Solution()
node = ListNode(3)
s.deleteNode(node)

