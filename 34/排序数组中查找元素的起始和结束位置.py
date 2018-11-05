class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = (start + end) / 2
            if target == nums[mid]:
                p1 = mid
                p2 = mid
                while nums[p1] == nums[mid]:
                    p1 = p1 - 1
                    if p1 < 0:
                        break
                while nums[p2] == nums[mid]:
                    p2 = p2 + 1
                    if p2 > len(nums) - 1:
                        break
                return [p1 + 1, p2 - 1]
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = end - 1
        return[-1, -1]

nums = [1]
target = 1
a = Solution().searchRange(nums, target)