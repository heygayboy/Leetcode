class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        start = end = 0
        max_len = 0
        for (i, num) in enumerate(nums):
            if i == 0:
                pre = num
                continue
            else:
                cur = num
                if cur > pre:
                    pre = cur
                    end = i + 1
                    length = end - start
                else:
                    pre = cur
                    end = i
                    length = end - start
                    start = i
                max_len = max(max_len, length)

        return max_len

nums = [1,3,5,4,2,3,4,5]
Solution().findLengthOfLCIS(nums)