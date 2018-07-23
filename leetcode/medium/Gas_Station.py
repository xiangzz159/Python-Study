# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/7/16 16:22

@desc: https://leetcode-cn.com/problems/gas-station/description/

'''


class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        index_list = []
        for i in range(l):
            if gas[i] < cost[i]:
                continue
            g = gas[i] + gas[(i + 1) % l] - cost[i] - cost[(i + 1) % l]
            if g > 0:
                index_list.append(i)
        if len(index_list) == 0:
            return -1
        ng = 0
        for index in index_list:
            for i in range(index, l + index):
                ng = ng + gas[i % l] - cost[i % l]
                if ng < 0:
                    break
            if ng >= 0:
                return index
        return -1

    def canCompleteCircuit2(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, total, tank = 0, 0, 0
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return -1 if (total + tank < 0) else start



if __name__ == '__main__':
    s = Solution()
    # i = s.canCompleteCircuit([6, 1, 4, 3, 5], [3, 8, 2, 4, 2])
    # i = s.canCompleteCircuit([6, 1, 4, 3, 5], [3, 8, 2, 4, 2])
    # i = s.canCompleteCircuit([5], [5])
    # i = s.canCompleteCircuit([3, 3, 4], [3, 4, 4])
    i = s.canCompleteCircuit2(
        [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
         95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
         25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
         53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66],
        [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
         55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
         83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
         13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
    print(i)
