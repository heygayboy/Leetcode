# -*- coding: utf-8 -*-
'''
这种方法超出时间限制
因为回溯法回溯了全部的可能性
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        string = [A, B, C, D]
        length = len(A)

        def cal_sum(answer, string):
            subset_sum = 0

            for i in range(len(answer)):
                subset_sum = subset_sum + string[i][answer[i]]
            return subset_sum

        def subset(string, answer, step, count):
            if step == len(string):
                temp = cal_sum(answer, string)
                if temp ==0:
                    count = count + 1
            else:
                for i in range(length):
                    answer[step] = i
                    count = subset(string, answer, step + 1, count)
            return count

        answer = [0] * len(string)
        count = 0
        Sum = subset(string, answer, 0, count)
        return Sum

A = [1,2]
B = [-2,-1]
C = [-1,2]
D = [0,2]
count = Solution().fourSumCount(A, B, C, D)
print(count)
