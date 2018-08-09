# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/9 9:17

@desc:

'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        obstacleGrid_ = [[0 for i in range(col)] for j in range(row)]
        obstacleGrid_[0][0] = (obstacleGrid[0][0] + 1) % 2
        for i in range(1, col):
            if obstacleGrid[0][i] == 1:
                obstacleGrid_[0][i] = 0
            else:
                obstacleGrid_[0][i] = obstacleGrid_[0][i - 1]
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                obstacleGrid_[i][0] = 0
            else:
                obstacleGrid_[i][0] = obstacleGrid_[i - 1][0]
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid_[i][j] = 0
                else:
                    obstacleGrid_[i][j] = obstacleGrid_[i - 1][j] + obstacleGrid_[i][j - 1]
        return obstacleGrid_[row - 1][col - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([
        [0]
    ]))
