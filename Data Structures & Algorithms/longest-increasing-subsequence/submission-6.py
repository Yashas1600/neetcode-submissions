class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dp(i,prevIdx):
            if i == len(nums):
                return 0    
            if (i, prevIdx) in memo:
                return memo[(i, prevIdx)]
            
            result = dp(i + 1, prevIdx)

            if prevIdx == -1 or nums[i] > nums[prevIdx]:
                result = max(result, 1+ dp(i+ 1, i))
            memo[(i,prevIdx)] = result
            return result

        return dp(0,-1)

        