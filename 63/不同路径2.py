class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        re_array = np.zeros((m, n))
        if obstacleGrid[0][0]:
            re_array[0, 0] = 0
        else:
            re_array[0, 0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0]:
                re_array[i, 0] = 0
            else:
                re_array[i, 0] = re_array[i - 1, 0]
        for j in range(1, n):
            if obstacleGrid[0][j]:
                re_array[0, j] = 0
            else:
                re_array[0, j] = re_array[0, j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    re_array[i, j] = 0
                else:
                    re_array[i, j] = re_array[i - 1, j] + re_array[i, j - 1]
        return int(re_array[m - 1, n - 1])

obstacleGrid = [[0,1]]
a = Solution().uniquePathsWithObstacles(obstacleGrid)