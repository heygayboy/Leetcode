class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            if start == end:
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if target < nums[start]:
            return start
        elif target > nums[start]:
            return start + 1
        else:
            return start


nums = [1,3,5,6]
target = 0
a = Solution().searchInsert(nums, target)
print (a)