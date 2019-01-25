# -*- coding: utf-8 -*-


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def ksize_set(answer, k):
            count = 0
            for i in range(len(answer)):
                if answer[i]:
                    count = count + 1
            return count == k

        def display_outcome(answer, set):
            global result
            res = []

            for i in range(len(answer)):
                if answer[i]:
                    res.append(set[i])
            result.append(res)

        def subset(set, answer, step, k):
            if step == len(set):
                if ksize_set(answer, k):
                    display_outcome(answer, set)
            else:
                for i in range(2):
                    answer[step] = i
                    subset(set, answer, step + 1, k)

        set = range(1, n + 1)
        global result
        result = []
        answer = [0] * len(set)
        subset(set, answer, 0, k)
        return result