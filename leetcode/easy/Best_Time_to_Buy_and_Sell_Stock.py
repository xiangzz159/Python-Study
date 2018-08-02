# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/2 14:44

@desc: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/

'''


class Solution(object):
    def maxProfit1(self, prices):
        """
        暴力求解
        :type prices: List[int]
        :rtype: int
        """
        max_num = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > 0:
                    max_num = max(max_num, prices[j] - prices[i])
        return max_num

    def maxProfit2(self, prices):
        """
        动态规划
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min_num = prices[0]
        ret = 0
        for i in range(1, len(prices)):
            ret = max(ret, prices[i] - min_num)
            min_num = min(min_num, prices[i])
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit1([7,1,5,3,6,4]))
