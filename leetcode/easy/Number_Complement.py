#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'476. Number Complement'


def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num