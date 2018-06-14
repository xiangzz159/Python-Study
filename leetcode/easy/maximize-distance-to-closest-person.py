#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/6/13 17:42

@desc: https://leetcode-cn.com/contest/weekly-contest-88/problems/maximize-distance-to-closest-person/

'''

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        num_list = []
        for i in range(len(seats)):
            if seats[i] == 1:
                num_list.append(i)
        m = len(num_list)
        pre = num_list[0]
        res = max(num_list[0] - 0, len(seats) - 1 - num_list[m - 1])
        for i in range(1, m):
            res = max(res, (num_list[i] - pre) / 2)
            pre = num_list[i]
        return int(res)



if __name__ == '__main__':
    # t1 = time.time()
    s = Solution()
    str = s.maxDistToClosest([1,0,0,0])
    print(str)
    # print(time.time() - t1)