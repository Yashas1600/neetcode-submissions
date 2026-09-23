class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}


        """
        5:
        
        """

        def dp(i):
            if i == 1:
                return 1
            if i in memo:
                return memo[i]
            
            result = 0
            for j in range(1,i):
                result = max(result, (i-j) * j, j * dp(i - j))
            memo[i] = result
            return result
        return dp(n)

            

        