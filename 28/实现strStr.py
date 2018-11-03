class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        for index_num in range(len(haystack)):
            if haystack[index_num] == needle[0]:
                flag = 1
                if (len(haystack) - index_num) < len(needle):
                    return -1
                else:
                    for i in range(len(needle)):
                        if haystack[index_num + i] != needle[i]:
                            flag = 0
                    if flag:
                        return index_num
        return -1

haystack = "mississippi"
needle = "issip"
solution = Solution().strStr(haystack, needle)