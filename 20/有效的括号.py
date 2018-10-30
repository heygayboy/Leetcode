# -*- coding: utf-8 -*-


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbol_list = []
        symbol_dict = {')': '(', ']': '[', '}': '{'}
        for symbol in s:
            if symbol == '(' or symbol =='[' or symbol == '{':
                symbol_list.append(symbol)
            else:
                if symbol_list == []:
                    return False
                else:
                    pop_symbol = symbol_list.pop()
                    if pop_symbol != symbol_dict[symbol]:
                        return False
        if symbol_list == []:
            return True
        else:
            return False

s = ']'
result = Solution().isValid(s)
print(result)