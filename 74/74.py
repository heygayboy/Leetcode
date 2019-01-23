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

        for row in range(m):
            if target < matrix[row][0] or target > matrix[row][n-1]:
                continue
            else:
                p1 = 0
                p2 = n - 1
                while p1 <= p2:

                    p = (p1 + p2)/2

                    if matrix[row][p] < target:
                        p1 = p + 1  #注意这里要+1
                    elif matrix[row][p] > target:
                        p2 = p - 1
                    else:
                        return True
                return False
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 13
Solution().searchMatrix(matrix, target)