# -*- coding: utf-8 -*-

'''
傻瓜法
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            num_list = []
            real_number = x
            while x:
                num_list.append(x % 10)
                x = x / 10

            number = 0
            for num in num_list:
                number = number * 10 + num
            if number == real_number:
                return True
            else:
                return False

