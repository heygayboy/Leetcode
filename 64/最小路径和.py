class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        import numpy as np
        m = len(grid)
        n = len(grid[0])

        re_array = np.zeros((m, n))
        re_array[0, 0] = grid[0][0]

        for i in range(1, m):
            re_array[i, 0] = re_array[i - 1, 0] + grid[i][0]
        for j in range(1, n):
            re_array[0, j] = re_array[0, j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                re_array[i, j] = min(re_array[i-1, j], re_array[i, j-1]) + grid[i][j]
        return int(re_array[m - 1, n - 1])


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
a = Solution().minPathSum(grid)