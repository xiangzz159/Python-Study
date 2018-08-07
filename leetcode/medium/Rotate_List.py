#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/7 14:45

@desc:

'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        root = head
        l = 1
        while root.next is not None:
            l += 1
            root = root.next
        k = k % l
        if k == 0:
            return head

        root = head
        begin = root
        for i in range(l - k - 1):
            root = root.next
        next_node = root.next
        root.next = None
        re = next_node
        re_node = re
        while re.next is not None:
            re = re.next
        re.next = begin
        return re_node

if __name__ == '__main__':
    node = ListNode(1)
    root = node
    for i in range(2, 6):
        node.next = ListNode(i)
        node = node.next

    root = ListNode(None)
    s = Solution()
    s.rotateRight(root, 0)

