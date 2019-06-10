# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1

        a0 = 0
        a1 = 1

        while n-1 > 0:
            n = n - 1
            temp = a0 + a1
            a0 = a1
            a1 = temp
        return temp
