class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        """
        to find ways to make 3:
        need way to make 2 and 1
        asks us num of ways not the actual ways so its a dp problem not
        backtracking problem


        """

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]
                
        