class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        for i in range(len(nums)):

            while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                index = nums[i] - 1
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

nums = [-1,4,2,1,9,10]
Solution().firstMissingPositive(nums)
