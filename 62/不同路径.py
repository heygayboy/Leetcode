class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import numpy as np
        re_array = np.zeros((m, n))
        re_array[0, :] = 1
        re_array[:, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                re_array[i, j] = re_array[i - 1, j] + re_array[i, j - 1]
        return int(re_array[m - 1, n - 1])


m = 3
n = 2
a = Solution().uniquePaths(m, n)