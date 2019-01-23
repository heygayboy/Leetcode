#!/usr/bin/python
# coding:utf-8


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num0 = 0
        num1 = 0
        num2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num0 = num0 + 1
            elif nums[i] == 1:
                num1 = num1 + 1
            else:
                num2 = num2 + 1

        for i in range(len(nums)):
            if i < num0:
                nums[i] = 0
            elif i < num1 + num0:
                nums[i] = 1
            else:
                nums[i] = 2
