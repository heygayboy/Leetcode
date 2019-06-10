# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        low = 0
        high = len(rotateArray) - 1
        if rotateArray[low] <= rotateArray[high]:
            return rotateArray[low]
        while (high - low > 1):
            p = (low + high) / 2

            if rotateArray[p] <= rotateArray[low] and rotateArray[p] <= rotateArray[high]:
                high = p
            elif rotateArray[p] >= rotateArray[low] and rotateArray[p] >= rotateArray[high]:
                low = p
        return rotateArray[high]

rotateArray = [ 1,1,1,111,1]
a = Solution().minNumberInRotateArray(rotateArray)