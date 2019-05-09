# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/2 15:14

@desc: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size <= 1:
            return 0
        max_ = 0
        for i in range(1, size):
            max_ += prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0
        return max_


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))