#!/usr/bin/python
# coding:utf-8


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        row = 0
        column = n-1

        while row <= m -1 and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                row = row + 1
            else:
                column = column - 1

        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20
Solution().searchMatrix(matrix, target)