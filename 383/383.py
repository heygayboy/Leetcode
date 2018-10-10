# -*- coding: utf-8 -*-

'''
题目分析：统计 ransomNote和 magazine中各字母出现的次数
要求 ransomNote中小于等于 magazine中
'''


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def count(string):
            count_list = [0] * 26
            for letter in string:
                idx = ord(letter) - ord('a')
                count_list[idx] = count_list[idx] + 1
            return count_list

        ransomNote_count_list = count(ransomNote)
        magazine_count_list = count(magazine)
        for (num1, num2) in zip(ransomNote_count_list, magazine_count_list):
            if num1 > num2:
                return False
        return True



