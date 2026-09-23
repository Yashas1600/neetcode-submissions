class Solution:
    def numDecodings(self, s: str) -> int:
        """


        """

        # number of ways to memoize from this index
        memo = {}
        memo[len(s)] = 1

        if s[0]== '0':
            return 0


        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            result = dp(i + 1)

            if valid2Digits(s[i:i + 2]):
                result += dp(i + 2)
            memo[i] = result
            return result 

        def valid2Digits(s):
            if len(s) != 2:
                return False
            if s[0] != '0' and int(s) <= 26:
                return True
        return dp(0)