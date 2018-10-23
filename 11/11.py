class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(height) - 1

        max_ = (len(height) - 1) * min(height[a], height[b])

        while a < b:
            if (height[a] < height[b]):
                a = a + 1
                temp = (b - a) * min(height[a], height[b])
                if temp > max_:
                    max_ = temp
            elif (height[a] > height[b]):
                b = b - 1
                temp = (b - a) * min(height[a], height[b])
                if temp > max_:
                    max_ = temp
            else:
                a = a + 1
                b = b - 1
                temp = (b - a) * min(height[a], height[b])
                if temp > max_:
                    max_ = temp
        return max_

solution = Solution()
s = [1,1]
solution.maxArea(s)