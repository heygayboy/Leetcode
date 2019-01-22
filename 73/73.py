#!/usr/bin/python
# coding:utf-8


'''空间复杂度o(m+n)
list_row和list_column用于存放哪一行有0 那一列有0'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        list_row = [1] * m
        list_column = [1] * n

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    list_row[row] = 0
                    list_column[column] = 0

        for row in range(m):
            if list_row[row] == 0:
                for column in range(len(matrix[row])):
                    matrix[row][column] = 0

        for column in range(n):
            if list_column[column] == 0:
                for row in range(m):
                    matrix[row][column] = 0
        return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)