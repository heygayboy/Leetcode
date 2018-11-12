import copy


class Solution(object):
    def _permute(self, nums, p, res, used):
        if len(p) == len(nums):
            res.append(copy.copy(p))

        for i,_ in enumerate(nums):
            if not used[i]:
                p.append(nums[i])
                used[i] = True
                self._permute(nums, p, res, used)
                p.pop()
                used[i] = False


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, used = list(), list()
        if not nums:
            return result

        for _ in enumerate(nums):
            used.append(False)
        self._permute(nums, list(), result, used)
        return result


nums = [1,2,3]
res = Solution().permute(nums)
print(res)
