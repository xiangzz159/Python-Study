#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/2/4 15:30

@desc: 771. Jewels and Stones

'''


def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    num = 0
    for s in S:
        for j in J:
            if j == s:
                num += 1
    return num


if __name__ == '__main__':
    num = numJewelsInStones("aAn", "aaAAAjeNNnn")
    print(num)
