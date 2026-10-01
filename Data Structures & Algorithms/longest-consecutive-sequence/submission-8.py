class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        maxCount = 0
        for num in seen:
            if num -1 in seen:
                continue
            i = 1
            curCount = 1
            while (num + i) in seen:
                i += 1
                curCount += 1
            maxCount = max(maxCount, curCount)
        return maxCount 
