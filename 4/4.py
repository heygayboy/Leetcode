# -*- coding: utf-8 -*-

'''
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n))
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import numpy as np
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        result = []
        p1 = 0
        p2 = 0
        while p1 < len_nums1 and p2 < len_nums2:
            num1 = nums1[p1]
            num2 = nums2[p2]
            if num1 <= num2:
                result.append(num1)
                p1 = p1 + 1
            else:
                result.append(num2)
                p2 = p2 + 1

        while p1 < len_nums1:
            result.append(nums1[p1])
            p1 = p1 + 1

        while p2 < len_nums2:
            result.append(nums2[p2])
            p2 = p2 + 1

        length = len(result)
        if length % 2 !=0:
            medium = result[length/2]
            return float(medium)
        else:
            medium1 = result[length/2]
            medium2 = result[length/2 - 1]
            return float(medium1 + medium2)/2



nums1 = [1, 2]
nums2 = [3, 4]
Solution = Solution()
a = Solution.findMedianSortedArrays(nums1, nums2)