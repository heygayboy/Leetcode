class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums, reverse= False)
        tri_list = []
        if len(nums) < 3:
            return tri_list
        i = 0
        while i < len(nums) - 1:
            a = nums[i]
            target = 0 - a
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                sum = nums[p1] + nums[p2]
                if sum < target:
                    p1 = p1 + 1
                elif sum > target:
                    p2 = p2 - 1
                else:
                    temp_list = []
                    temp_list.append(a)
                    temp_list.append(nums[p1])
                    temp_list.append(nums[p2])

                    tri_list.append(temp_list)

                    while nums[p1] == temp_list[1] and p1 < p2:
                        p1 = p1 + 1
                    while nums[p2] == temp_list[2] and p1 < p2:
                        p2 = p2 - 1
            while nums[i] == a and i < len(nums) - 1:
                i = i + 1
        return tri_list


s = [0, 0, 0]
solution = Solution()
a = solution.threeSum(s)