# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/24 16:55

@desc:

'''

from math import sqrt


class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return 2
        while True:
            if self.is_palindrome(N) and self.is_prime(N):
                return N
            if N % 2 == 0:
                N += 1
            else:
                N += 2

    def is_prime(self, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_palindrome(self, n):
        ans = 0
        N = n
        while N > 0:
            ans = ans * 10 + N % 10
            N = int(N / 10)
        return ans == n

    def primePalindrome1(self, N):
        """
        :type N: int
        :rtype: int
        """

        def isPrime(x):
            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        if N <= 2:
            return 2
        if N == 6:
            return 7
        if 8 <= N <= 11:
            return 11
        for x in range(10 ** int(len(str(N)) / 2), 10 ** 5):
            y = int(str(x) + str(x)[-2:: -1])
            if y >= N and isPrime(y):
                return y


if __name__ == '__main__':
    s = Solution()
    re = s.primePalindrome1(102)
    print(re)
