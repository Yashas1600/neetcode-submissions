class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r,l = 0,0
        res = float("inf")
        sum = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                res = min(res, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1

        return res if res != float("inf") else 0




        