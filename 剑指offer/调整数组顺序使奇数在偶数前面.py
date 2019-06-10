# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        res_ou = []
        res_ji = []
        for num in array:
            if num % 2 == 0:
                res_ou.append(num)
            else:
                res_ji.append(num)
        res_ji.extend(res_ou)
        return res_ji

a = [1,2,3,4,5,6,7]
b = Solution().reOrderArray(array= a)
