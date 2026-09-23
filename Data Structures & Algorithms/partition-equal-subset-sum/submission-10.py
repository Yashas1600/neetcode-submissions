class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2

        memo = [[-1] * (target + 1) for i in range(len(nums) + 1)]

        def dp(i,target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            
            if memo[i][target] != -1:
                return memo[i][target]
                
            memo[i][target] = dp(i+1, target) or dp(i + 1, target - nums[i])


            return memo[i][target]


        return dp(0,target)

        
        