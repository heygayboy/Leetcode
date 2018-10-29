class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def write_answer(answer):
            # global result
            answer = ("".join(answer))
            result.append(answer)


        def zuhe_set(digits, answer, step):
            if step == len(digits):
                write_answer(answer)
                return result
            else:
                digit = digits[step]
                for i in range(len(fdict[digit])):
                    answer[step] = fdict[digit][i]
                    zuhe_set(digits, answer, step + 1)
        fdict = {'2': "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        answer = [0] * len(digits)
        result = []
        if digits == '':
            return []
        else:
            zuhe_set(digits, answer, 0)

            return result