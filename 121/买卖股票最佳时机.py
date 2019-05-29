# -*- coding: utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max = 0

        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > max:
                max = prices[i] - min

        return max


a= [7,1,5,3,6,4]
Solution().maxProfit(a)