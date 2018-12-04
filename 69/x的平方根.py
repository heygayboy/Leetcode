class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        p1 = 0
        p2 = x
        p = (p1 + p2) / 2

        while p1 <= p2:
            p = (p1 + p2) / 2

            if p * p == x:
                return p
            else:
                if p * p < x:
                    p1 = p + 1
                else:
                    p2 = p - 1
        if p * p <= x:
            return p
        else:
            return p - 1


x = 1
y = Solution().mySqrt(x)
