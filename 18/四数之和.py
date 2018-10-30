class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums, reverse=False)
        tri_list = []
        if len(nums) < 3:
            return tri_list
        i = 0
        while i < len(nums) - 2:
            a = nums[i]
            j = i + 1
            while j < len(nums) - 1:
                b = nums[j]
                target_num = target - a - b
                p1 = j + 1
                p2 = len(nums) - 1
                while p1 < p2:
                    sum = nums[p1] + nums[p2]
                    if sum < target_num:
                        p1 = p1 + 1
                    elif sum > target_num:
                        p2 = p2 - 1
                    else:
                        temp_list = []
                        temp_list.append(a)
                        temp_list.append(b)
                        temp_list.append(nums[p1])
                        temp_list.append(nums[p2])

                        tri_list.append(temp_list)

                        while nums[p1] == temp_list[2] and p1 < p2:
                            p1 = p1 + 1
                        while nums[p2] == temp_list[3] and p1 < p2:
                            p2 = p2 - 1
                while nums[j] == b and j < len(nums) - 1:
                    j = j + 1

            while nums[i] == a and i < len(nums) - 2:
                i = i + 1
        return tri_list


nums = [1, 0, -1, 0, -2, 2]
target = 0
solu = Solution()
tri_list = solu.fourSum(nums, target)
print(tri_list)