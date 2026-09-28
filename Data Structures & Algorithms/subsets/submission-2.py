class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        so this is a backtracking problem
        we have a descision tree where every step we decide if we wanna skip or use the element
        we dont wanna do duplicate values so maybe have a visited set
        base case is return when its visited or when len(cur) == len(nums)
        we are constantly editing an array so we should have like a res array andappend a copy of out subset
        then pop adn do like i + 1 to indicate not using it 
        if i == len (num) for question two , i should initiaize a dfs array whihc passes in a i value as well as the cur subset  does tha tsound good


        """
        #make sure to add a copy
        res = []
        i = 0
        cur = []
        def dfs(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)

        
        dfs(i,cur)
        return res
            


