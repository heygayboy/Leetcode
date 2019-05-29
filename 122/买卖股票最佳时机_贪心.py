# -*- coding: utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (not prices) or (len(prices) == 1):
            return 0

        res = 0
        for i in range(len(prices)-1):
            chajia = prices[i + 1] - prices[i]
            if chajia > 0:
                res = res + chajia

        return res
