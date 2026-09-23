class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp memoization bc we need to know the amount of money u can ronb max, and that ned to know the prev max
        """

        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            result = max(nums[i] + dp(i + 2), dp(i + 1))
            memo[i] = result
            return memo[i]

        return dp(0)