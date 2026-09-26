class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        """

        """
        l,r =1, max(piles)
        res = max(piles)
        while l <= r:
            sum = 0
            m = (r + l)//2
            for p in piles:
                sum += math.ceil(p/m)
            if sum <= h:
                res = min(res, m)
                r = m - 1 
            else:
                l = m + 1
        return res
                
            
