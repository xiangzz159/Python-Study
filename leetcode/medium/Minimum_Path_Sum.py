# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/8 15:37

@desc:

'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)  # 行
        col = len(grid[0])  # 列
        grid_ = [[0 for i in range(col + 1)] for i in range(row + 1)]
        for i in range(row):
            for j in range(col):
                num = grid[i][j]
                num1 = grid_[i][j + 1]
                num2 = grid_[i + 1][j]
                if i == 0 and j == 0:
                    grid_[i + 1][j + 1] = num
                elif i == 0 and j != 0:
                    grid_[i + 1][j + 1] = num + num2
                elif j == 0 and i != 0:
                    grid_[i + 1][j + 1] = num + num1
                else:
                    grid_[i + 1][j + 1] = min((num1 + num), (num2 + num))
        return grid_[row][col]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[0, 2, 2, 6, 4, 1, 6, 2, 9, 9, 5, 8, 4, 4], [0, 3, 6, 4, 5, 5, 9, 7, 8, 3, 9, 9, 5, 4],
                        [6, 9, 0, 7, 2, 2, 5, 6, 3, 1, 0, 4, 2, 5], [3, 8, 2, 3, 2, 8, 8, 7, 5, 9, 6, 3, 4, 5],
                        [4, 0, 1, 3, 9, 2, 0, 1, 6, 7, 9, 2, 8, 9], [6, 2, 7, 9, 0, 9, 5, 2, 7, 5, 1, 4, 4, 7],
                        [9, 8, 3, 3, 0, 6, 8, 0, 8, 8, 3, 5, 7, 3], [7, 7, 4, 5, 9, 1, 5, 0, 2, 2, 2, 1, 7, 4],
                        [5, 1, 3, 4, 1, 6, 0, 4, 3, 8, 4, 3, 9, 9], [0, 6, 4, 9, 4, 1, 5, 5, 4, 2, 5, 7, 4, 0],
                        [0, 1, 6, 6, 4, 9, 2, 7, 8, 2, 1, 3, 3, 7], [8, 4, 9, 9, 2, 3, 8, 6, 6, 5, 4, 1, 7, 9]]))
