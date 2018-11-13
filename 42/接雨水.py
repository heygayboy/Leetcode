class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_p = [0] * len(height)
        right_p = [0] * len(height)

        for i in range(1, len(height)):
            left_p[i] = max(left_p[i - 1], height[i - 1])
        for i in reversed(range(len(height) - 1)):
            right_p[i] = max(right_p[i + 1], height[i + 1])

        res = 0
        for i in range(len(height)):
            if height[i] < left_p[i] and height[i] < right_p[i]:
                res = res + min(left_p[i], right_p[i]) - height[i]
        return res

height = [2,0,2]
a = Solution().trap(height)
