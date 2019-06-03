# -*- coding:utf-8 -*-
'''
问题的关键在于查找是从数组的左下角开始的
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == [] or array == [[]]:
            return False
        m = len(array)
        n = len(array[0])

        if target < array[0][0] or target > array[m-1][n-1]:
            return False

        i = m-1
        j = 0

        while i >= 0 and j < n:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                j = j + 1
            else:
                i = i - 1

        return False

target = 16
array = [[]]
A = Solution().Find(target, array)