# -*- coding: utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def cal_sum(answer, set):
            subset_sum = 0

            for i in range(len(answer)):
                if answer[i]:
                    subset_sum = subset_sum + set[i]
            return subset_sum

        def ksize_set(answer, k):
            count = 0
            for i in range(len(answer)):
                if answer[i]:
                    count = count + 1
            return count == k

        def count_num(answer, step, select):
            count = 0
            for i in range(step):
                if answer[i]:
                    count = count + 1
            if select:
                count = count + 1
            return count

        def subset(set, answer, k, step, minnum, target_num):
            if step == len(set):
                if ksize_set(answer, k):
                    temp = cal_sum(answer, set)
                    if abs(temp - target_num) < abs(minnum - target_num):
                        minnum = temp
            else:
                for i in range(2):
                    if count_num(answer, step, i) <= k:
                        answer[step] = i
                        minnum = subset(set, answer, k, step + 1, minnum, target_num)
            return minnum

        minnum = 0
        answer = [0] * len(nums)
        minnum = subset(nums, answer, 3, 0, minnum, target)
        return minnum

s = [0, 0, 0, 10, 55, 70, 80, 90]
solution = Solution()
target = 154
a = solution.threeSumClosest(s, target)
print(a)