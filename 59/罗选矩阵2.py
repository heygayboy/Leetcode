#coding=utf-8
'''
本体解法参考54题
'''
import numpy as np


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        n_list = range(n*n, 0, -1)

        x1, y1, x2, y2 = 0, 0, n-1, n-1
        res = np.zeros((n, n), dtype= np.int32)

        while x1 < x2 and y1 < y2 and n_list:
            for i in range(x1, x2):
                num = n_list.pop()
                res[y1][i] = num
            for i in range(y1, y2):
                res[i][x2] = n_list.pop()
            for i in range(x2, x1, -1):
                res[y2][i] = n_list.pop()
            for i in range(y2, y1, -1):
                res[i][x1] = n_list.pop()
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        if n_list != []:
            res[n/2][n/2] = n_list.pop()
        return res.tolist()


res = Solution().generateMatrix(5)
