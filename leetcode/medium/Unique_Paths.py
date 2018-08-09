#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/8 16:42

@desc: https://leetcode-cn.com/problems/unique-paths/description/

'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            grid[0][i] = 1
        for i in range(1, n):
            grid[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[n - 1][m - 1]



if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))