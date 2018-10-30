# -*- coding: utf-8 -*-
'''
所以可以采用二分的思路：
把四个区间分成两组：A、B一组，C、D一组，先从A、B组枚举出从两组中各取一个整数相加所有可能的结果，
将这些和排序（将这个排好序的vector记为ab），再枚举出C、D一组的所有情况，每算出一个c+d，就在ab中寻找是否存在c+d的相反数，
由于ab是已排序的，所以可以采用二分搜索的方式。考虑到ab可能存在重复的和，所以利用标准库的upper_bound 和lower_bound来求出重复的数有多少个
---------------------
作者：MonoTali
来源：CSDN
原文：https://blog.csdn.net/MonoTali/article/details/61627894
版权声明：本文为博主原创文章，转载请附上博文链接！
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def access(answer, n):
            temp_num = 0
            temp_sum = 1
            for i in answer:
                temp_sum = temp_sum + i
                if temp_sum < 0:
                    return False
                if i == 1:
                    temp_num = temp_num + i
            if temp_num == (n - 1):
                return True
            else:
                return False

        def generate(answer, step, result, n):
            if step == 2 * (n - 1):
                if access(answer, n):
                    temp_list = ['(']
                    for ch in answer:
                        if ch == 1:
                            temp_list.append('(')
                        else:
                            temp_list.append(')')
                    temp_list.append(')')
                    result.append(''.join(temp_list))
            else:
                for i in range(2):
                    if i == 0:
                        answer[step] = 1
                    else:
                        answer[step] = -1
                    result = generate(answer, step + 1, result, n)
            return result

        result = []

        '''[0]代表 ‘)’ [-1]代表 ‘(’'''
        answer = [0] * (2 * (n - 1))

        result = generate(answer, 0, result, n)
        return result


result = Solution().generateParenthesis(3)
print(result)