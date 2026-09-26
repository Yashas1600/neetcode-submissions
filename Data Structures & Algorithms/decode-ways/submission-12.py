class Solution:
    def numDecodings(self, s: str) -> int:

        """
        so the choice is gonna be to either include it or not to inlcude it 


        memoizing the number of ways to decode from each index


        """
        memo = {}

        def valid2Digit(i):
            if i + 1 >= len(s):
                return False
            if s[i] == "0":
                return False
            if s[i] == "1":
                return True
            if s[i] == "2" and s[i + 1] in ["0","1","2","3","4","5","6"]:
                return True
            return False

        def dp(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0

            result = dp(i + 1)
            if valid2Digit(i):
                result += dp(i + 2)
            memo[i] = result
            return result
        return dp(0)
            
