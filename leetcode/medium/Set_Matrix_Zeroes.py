# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/8/23 13:52

@desc: https://leetcode-cn.com/problems/set-matrix-zeroes/description/

'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 and col == 0:
            return matrix
        row_list = set([])
        col_list = set([])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_list.add(i)
                    col_list.add(j)
        for i in range(row):
            for j in range(col):
                if i in row_list or j in col_list:
                    matrix[i][j] = 0
        print(matrix)

if __name__ == '__main__':
    s = Solution()
    re = s.setZeroes([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
