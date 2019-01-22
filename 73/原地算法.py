#!/usr/bin/python
# coding:utf-8


'''空间复杂度o(1)

上面的算法是一种 O(m + n) 时间复杂度的算法，那有没有更好的算法呢？我们先来假设一种情况，比如说如果矩阵 T 的每一行都有一个 0 的话（如果从每一列来考虑，逻辑是一样的），那么是不是就可以把整个矩阵都置为 0 呢？根据题意，当然是可行的。
那么如果并不是每一行都有 0 呢？基于上面方案一的思路，我们知道我们需要用一些标记来标识某一行或是某一列是否存在 0。其实上面的思路是可以再精简一些。比如我们把标识行存在 0 的标识数组除掉，留下列的数组。这样当我们获得列标识数组 Flag-C 之后，再遍历矩阵 T，先把有 0 的行全部置 0，再把数组 Flag-C 标记的 0 所在的列进行置 0。过程如下图所示：
找到一个没有 0 的行，用来当成上面的标记数组 Flag-C，将有 0 的列所在的位置重置为 0
---------------------
作者：Q-WHai
来源：CSDN
原文：https://blog.csdn.net/lemon_tree12138/article/details/51176153
版权声明：本文为博主原创文章，转载请附上博文链接！

'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for row in range(m):
            flag = 1
            for column in range(n):
                if matrix[row][column] == 0:    flag = 0
            if flag == 1:
                break

        if row == m-1 and flag == 0:
            for row in range(m):
                for column in range(n):
                    matrix[row][column] = 0
        else:
            row_index = row
            for column in range(n):
                for row in range(m):
                    if matrix[row][column] == 0:
                        matrix[row_index][column] = 0
            for row in range(m):
                if row == row_index:
                    continue
                else:
                    for column in range(n):
                        if matrix[row][column] == 0:
                            matrix[row] = [0] * n

            for column in range(n):
                if matrix[row_index][column] == 0:
                    for row in range(m):
                        matrix[row][column] = 0


matrix = [[1]]
Solution().setZeroes(matrix)