# -*- coding: utf-8 -*-
'''

用双指针实现
一个指针用于遍历，一个指针用于记录新列表的元素
如果p1遍历到了新元素，p2 = p2 + 1在这个位置并且记录下来新元素

'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        p1 = 0
        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 = p1 + 1
                nums[p1] = nums[p2]
        return p1 + 1

