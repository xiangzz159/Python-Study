#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/30 17:43

@desc: https://leetcode-cn.com/problems/linked-list-cycle/description/

'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        sp = head
        fp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                return True

        return False
