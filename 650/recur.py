
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 2
        if n ==3:
            return 3
        for j in reversed(range(2, n)):
            if (n % j == 0):
                return min(n, self.minSteps(j) + n / j)
        return n



solution = Solution()
print(solution.minSteps(10))