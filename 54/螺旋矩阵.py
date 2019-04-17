#coding=utf-8
'''
每次转一圈之后改变四个顶点的坐标
进行下一次循环
记对角点坐标为（x1, y1）（x2, y2）
参考博客：
https://blog.csdn.net/qq_17550379/article/details/83148050
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res

        m = len(matrix)
        n = len(matrix[0])

        #初始化（x1, y1）（x2, y2）位置
        x1 = 0
        y1 = 0
        x2 = n - 1
        y2 = m - 1

        #循环开始
        while x1 <= x2 and y1 <= y2:
            '''（x1, y1）--->（x1, y2）'''
            for i in range(x1, x2 + 1):
                res.append(matrix[y1][i])
            '''（x1, y2）--->（x2, y2）'''
            for i in range(y1+1, y2+1):
                res.append(matrix[i][x2])
            '''（x2, y2）--->（x1, y2）'''
            for i in range(x2-1, x1, -1):
                res.append(matrix[y2][i])
            '''（x1, y2）--->（x1, y1）'''
            for i in (y2, y1, -1):
                res.append(matrix[i][x1])

            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        return res

