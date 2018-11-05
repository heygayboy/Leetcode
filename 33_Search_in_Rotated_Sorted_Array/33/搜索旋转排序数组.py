# -*- coding: utf-8 -*-

'''
注意这个解法过于复杂，实际上二分法的本质只要确定数字target位于左边还是右边即可
无需指定必须用于单调数组，所以无需确定左边单调或者右边单调后使用 erfen(s, target)
只需要把指针调整至相应位置即可

二分法几个易错点：
while p1 <= p2:的等号
end = mid - 1注意加一减一因为mid已经被判断过不是target了（不然会陷入死循环 start = end = mid)

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def erfen(s, target):
            p1 = 0
            p2 = len(s) - 1
            while p1 <= p2:
                p3 = (p1 + p2) / 2
                if s[p3] == target:
                    return p3
                elif target < s[p3]:
                    p2 = p3 - 1
                else:
                    p1 = p3 + 1
            return -1

        if len(nums) == 0:
            return -1

        i = 0
        j = len(nums) - 1
        if target < nums[i] and target > nums[j]:
            return -1
        else:
            while i <= j:
                p = (i + j) / 2
                if target == nums[p]:
                    return p
                if nums[p] > nums[i]:
                    if target <= nums[p] and target >= nums[i]:
                        if erfen(nums[i:p], target) == -1:
                            return -1
                        else:
                            return i + erfen(nums[i:p], target)
                    else:
                        i = p + 1
                else:
                    if target >= nums[p] and target <= nums[j]:
                        if erfen(nums[p + 1:j + 1], target) == -1:
                            return -1
                        else:
                            return p + 1 + erfen(nums[p + 1:j + 1], target)
                    else:
                        j = p - 1
            return -1
s = [3, 1]
target = 1
a = Solution().search(s, target)