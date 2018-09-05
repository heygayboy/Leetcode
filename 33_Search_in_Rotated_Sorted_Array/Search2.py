class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high :
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[low] < nums[mid]:
                    if target < nums[mid] and target >= nums[low]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if target > nums[mid] and target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid + 1
        return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))