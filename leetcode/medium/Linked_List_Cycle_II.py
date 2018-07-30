#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/30 16:57

@desc: https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
https://blog.csdn.net/willduan1/article/details/50938210

'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        fp = head
        sp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                break
        if fp is None or fp.next is None:
            return None
        sp = head
        while fp != sp:
            sp = sp.next
            fp = fp.next
        return sp

if __name__ == '__main__':
    s = Solution()