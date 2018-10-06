class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        minStep = list()
        for i in range(0, n):
            minStep.append(i + 1)
        minStep[0] = 0

        for i in range(4, n + 1):
            for j in range(2, i):
                if (i % j == 0):
                    minStep[i - 1] = min(minStep[i - 1], minStep[j - 1] + i / j)

        return minStep[n - 1]

solution = Solution()
print(solution.minSteps(6))