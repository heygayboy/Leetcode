class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def trans_to_int(list_num):
            if len(list_num) != 2:
                raise ValueError("LEN IS NOT 2")
            a = int(list_num[0])
            b = int(list_num[1])
            return int(a*10 + b)

        solu = [0] * len(s)
        if s[0] == '0':
            s[0] = 0
        else:
            solu[0] = 1

        if len(s) >= 2:
            if trans_to_int(s[0:2]) < 26:
                solu[1] = 2
            else:
                solu[1] = 1

        for n in range(2, len(s)):
            if s[n-1] == '0' and s[n] == '0':
                return 0
            if trans_to_int(s[n-1:n+1]) <= 26 and s[n-1] != '0' and s[n] != '0':
                solu[n] = solu[n-1] + solu[n-2]
            elif s[n-1] == '0':
                solu[n] = solu[n-2]
            elif s[n] == '0':
                solu[n] = solu[n-1]
        return solu[-1]



if __name__ == '__main__':
        s = '226'
        Solution().numDecodings(s)