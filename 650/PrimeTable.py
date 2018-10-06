import numpy as np


class Solution(object):
    def __init__(self):
        self.isPrime = self.getIsPrime()

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        else:
            isPrime = self.isPrime
            result = 0
            flag = True
            while flag:
                for i in range(n - 1):
                    if isPrime[i]:
                        if n % (i + 2) == 0:
                            n = n / (i + 2)
                            result = result + (i + 2)
                            if n == 1:
                                flag = False
                            else:
                                break
            return result

    def getIsPrime(self):
        isPrime = np.zeros((1001))
        isPrime[0] = 1
        for i in range(1, 1001):
            number = i + 2
            flag = False
            for j in range(0, i):
                if isPrime[j] == 1:
                    if number % (j + 2) == 0:
                        flag = True
                        break
            if not flag:
                isPrime[i] = 1
        return isPrime

Solution = Solution()
print (Solution.minSteps(25))