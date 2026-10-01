class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        """
        pick on index which will iteraate from left to right
        then 

         [-1,0,1,2,-1,-4]
         [-4, -1,-1,0,1, 2]

         then im going start off by assuming we wil have a left pointer at i = 0 and a right pointer at i = len(nums) -1
        if left + max right <

        """
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            if nums[i]> 0:
                break
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
            
        