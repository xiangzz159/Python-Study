#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/15 16:52

@desc: https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/

'''

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2:
            return 0
        total_cost = [0] * len(cost)
        total_cost[0] = cost[0]
        total_cost[1] = cost[1]
        for i in range(2, len(cost)):
            total_cost[i] = min(total_cost[i - 1] + cost[i], total_cost[i - 2] + cost[i])
        return min(total_cost[len(cost) - 1], total_cost[len(cost) - 2])



if __name__ == '__main__':
    # t1 = time.time()
    s = Solution()
    b = s.minCostClimbingStairs([0,0,0,0])
    print(b)