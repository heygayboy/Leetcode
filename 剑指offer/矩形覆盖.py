# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        res_list = range(0, number+1)
        res_list[0] = 0
        res_list[1] = 1
        res_list[2] = 2
        for i in range(3, number+1):
            res_list[i] = res_list[i-1] + res_list[i-2]
        return res_list[number]



a = Solution().rectCover(10)
print(a)