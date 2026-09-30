class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        [1,2,4,6]
        [1,1,1,1]
        forward pass

        [1,2,4,6]
        

        backward pass
        [1,2,8,48]
                6

        """

        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


