class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

        some how have to incorporate the negatives and the positive bc what if its -2,2 -5, -1 -10, 0, 2, 5
        store with a tuple
        """

        memo = {}

        def dp(i):
            if i == 0:
                memo[i] = (nums[0], nums[0])
                return memo[i]
            prevMin, prevMax = memo[i-1]
            curMin = min(nums[i],prevMin * nums[i], prevMax * nums[i])
            curMax = max(nums[i], prevMin * nums[i], prevMax * nums[i])

            memo[i] = (curMin, curMax)
            return memo[i]
        result = float("-inf")
        for i in range(len(nums)):
            curMin, curMax = dp(i)
            result = max(curMax, result)
        return result