class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0
        p2 = 0
        if nums == []:
            return 0
        while p1 < len(nums):
            if nums[p1] != val:
                nums[p2] = nums[p1]
                p2 = p2 + 1
            p1 = p1 + 1
        return p2