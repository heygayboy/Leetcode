class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums = [0] * len(nums)
        max_nums[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if max_nums[i - 1] + nums[i] > nums[i]:
                max_nums[i] = max_nums[i - 1] + nums[i]
            else:
                max_nums[i] = nums[i]

            if max_nums[i] > res:
                res = max_nums[i]

        return res
