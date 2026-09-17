class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l = 1
        r = max(piles)
        res = r
        while l<= r:
            sum = 0
            k = (r + l) //2
            for p in piles:
                sum += math.ceil(p/k)
            if sum <= h:
                r = k - 1
                res = min(res, k)
                
            else:
                l = k+1

        return res