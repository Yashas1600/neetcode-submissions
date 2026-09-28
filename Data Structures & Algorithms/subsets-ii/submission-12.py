class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """

        """

        res = []
        nums.sort()
        def dfs(i,cur):
            if cur in res:
                return
            if i == len(nums):
                res.append(cur.copy())
                return 
          
            cur.append(nums[i])
            dfs(i + 1,cur)
            cur.pop()
            dfs(i + 1, cur)
        dfs(0,[])
        return res