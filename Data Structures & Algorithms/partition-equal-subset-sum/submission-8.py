class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = total//2
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for number in dp:
                nextDP.add(nums[i] + number)
                nextDP.add(number)
            dp = nextDP

               
        return True if target in dp else False