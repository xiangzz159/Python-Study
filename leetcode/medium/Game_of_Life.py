# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/23 16:43

@desc: https://leetcode-cn.com/problems/game-of-life/description/

'''


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        if row == 0 or col == 0:
            return
        for i in range(row):
            for j in range(col):
                num = self.getNeighbor(board, row, col, i, j)
                if num == 2:
                    continue
                elif num == 3:
                    board[i][j] = 3 if board[i][j] == 0 else 1
                else:
                    board[i][j] = 2 if board[i][j] == 1 else 0
        for i in range(row):
            for j in range(col):
                board[i][j] %= 2
        print(board)

    def getNeighbor(self, board_, rows, cols, x, y):
        sum = 0
        for i in range(x - 1, x + 2, 1):
            for j in range(y - 1, y + 2, 1):
                if i == x and j == y:
                    continue
                if i >= 0 and i < rows and j >= 0 and j < cols and (board_[i][j] == 1 or board_[i][j] == 2):
                    sum += 1
        return sum


if __name__ == '__main__':
    s = Solution()
    s.gameOfLife([
        [1, 1]
    ])
