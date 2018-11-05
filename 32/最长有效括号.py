class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        elif len(s) == 2:
            if s == '()':
                return 2
            else:
                return 0
        else:
            dp = [0] * len(s)
            dp[0] = 0
            stack = []
            if s[0] =='(':
                stack.append(s[0])

            for i in range(1, len(s)):
                if s[i] == '(':
                    stack.append(s[i])
                    dp[i] = 0
                else:
                    if stack == []:
                        dp[i] = 0
                    else:
                        dp[i] = dp[i - 1] + 2
                        if i - dp[i] > 0:
                            dp[i] = dp[i - dp[i]] + dp[i]
                        stack.pop()

            return max(dp)


s = "(()())"
a = Solution().longestValidParentheses(s)