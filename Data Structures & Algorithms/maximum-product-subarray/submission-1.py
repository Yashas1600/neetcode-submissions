class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]

        for i in range (1, len(nums)) :
            num = nums[i]
            theMax = max(num, curMax * num, curMin * num)
            theMin = min( num, curMin * num, curMax *  num)

            curMax = theMax
            curMin = theMin
            result = max(theMax, result)



        return result