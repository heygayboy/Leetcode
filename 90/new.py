class Solution(object):
    def subsetsWithDup(self, nums):
        def dfs(step, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)
            if step == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(step+1, i+1, valuelist + [nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])

        print(res)
        return res


if __name__ == '__main__':
    nums = [1,1,2,2]
    Solution().subsetsWithDup(nums)