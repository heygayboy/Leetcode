class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def add_to_list(nums, sorted_index, res_list):
            new_list = []
            for i in range(len(sorted_index)):
                if sorted_index[i] == 1:
                    new_list.append(nums[i])
            if new_list not in res_list:
                res_list.append(new_list)
            return res_list

        def crear_index(sorted_index, nums, res_list, step):
            if step == len(nums):
                res_list = add_to_list(nums, sorted_index, res_list)
            else:
                for i in range(len(nums)):
                    for j in [0, 1]:
                        sorted_index[i] = j
                        crear_index(sorted_index, nums, res_list, step + 1)
            return res_list

        res_list = []
        step = 0
        sorted_index = [0] * len(nums)
        res_list = crear_index(sorted_index, nums, res_list, 0)
        print(res_list)


if __name__ == '__main__':
    nums = [1,1,2,2]
    Solution().subsetsWithDup(nums)