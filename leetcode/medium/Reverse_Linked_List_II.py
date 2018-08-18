#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/14 10:36

@desc:

'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        q, p = None, head
        for i in range(m - 1):
            q = p
            p = p.next
        end = p
        pp = p
        qq = p.next
        for i in range(m, n):
            rr = qq.next
            qq.next = pp
            pp = qq
            qq = rr
        end.next = qq
        if q is not None:
            q.next = pp
        else:
            head = pp
        return head

if __name__ == '__main__':
    root = ListNode(1)
    head = root
    for i in range(2, 3):
        root.next = ListNode(i)
        root = root.next

    s = Solution()
    re = s.reverseBetween(head, 1, 2)




