class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        how would i iterate through the array?
        no repeat elements allowed

        
        [1,2,3]

        [1]
        [1]



        i htink you should pick an index i and then insert i -1 one before it after it and so on 
        base case is when size of cur array = len(nums) bc u have to use all elements

        """
        
        cur = []
        res = []
        if len(nums) == 0:
            return [[]]
        def dfs(i):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 
            for i in range(len(nums)):
                if nums[i] in cur:
                    continue
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res
            
                    
            