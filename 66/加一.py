class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 1
        for i in reversed(range(len(digits))):
            temp = digits[i] + c
            if temp >= 10:
                digits[i] = temp - 10
                c = 1
            else:
                digits[i] = temp
                c = 0
        if c == 1:
            digits = list([1]) + digits
        return digits


d = [9, 9]
a = Solution().plusOne(digits=d)