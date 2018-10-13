class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Hash_table = dict()
        for (i, num) in enumerate(nums):
            if Hash_table.has_key(target - num):
                return i, Hash_table[target - num]
            Hash_table[num] = i 
        return None