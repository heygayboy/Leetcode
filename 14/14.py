class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [''] or strs == []:
            return ''

        j = 0

        while 1:
            length = len(strs)
            flag = 0
            if j >= len(strs[0]):
                break
            temp = strs[0][j]
            for i in range(1, length):
                if j >= len(strs[i]):
                    flag = 1
                    break
                if strs[i][j] != temp:
                    flag = 1
                    break
            if flag == 0:
                j = j + 1
            else:
                break

        return strs[0][:j]




