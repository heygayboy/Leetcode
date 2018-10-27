class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums, reverse=False)
        tri_list = []
        if len(nums) < 3:
            return None
        i = 0
        sum = 0

        while i < len(nums) - 1:
            a = nums[i]
            p1 = i + 1
            p2 = len(nums) - 1


            while p1 < p2:
                temp = a + nums[p1] + nums[p2]
                if sum < target:
                    p1 = p1 + 1
                    if abs(temp - target) < abs(sum - target):
                        sum = temp
                elif sum > target:
                    p2 = p2 - 1
                    if abs(temp - target) < abs(sum - target):
                        sum = temp
                else:
                    return target
            i = i + 1
        return sum


s = [0, 0, 0, 10, 55, 70, 80, 90]
solution = Solution()
target = 154
a = solution.threeSumClosest(s, target)
print(a)