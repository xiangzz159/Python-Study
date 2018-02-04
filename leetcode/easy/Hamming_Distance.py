#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'461. Hamming Distance'

def hammingDistance(self, x, y):
    return bin(x^y).count('1')

if __name__=="__main__":
    num = hammingDistance(1, 1, 4)
    print(num)