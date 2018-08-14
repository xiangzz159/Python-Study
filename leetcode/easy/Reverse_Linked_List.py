#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/14 9:24

@desc:

'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        first = None
        second = head
        third = None
        while second is not None:
            third = second.next
            second.next = first
            first = second
            second = third
        return first

if __name__ == '__main__':
    root = ListNode(1)
    head = root
    for i in range(2, 10):
        root.next = ListNode(i)
        root = root.next

    s = Solution()
    re = s.reverseList(head)
