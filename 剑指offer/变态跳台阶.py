# -*- coding:utf-8 -*-


class Solution:
    def jumpFloorII(self, number):
        global sum_num
        # write code here
        if number == 0 or number == 1:
            return 1
        return 2 * self.jumpFloorII(number-1)





a = Solution().jumpFloorII(3)