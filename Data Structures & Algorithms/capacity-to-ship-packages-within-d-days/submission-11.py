class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        output = max(weights)
        while l <= r:
            day = 1
            limit = (l + r)//2
            curLimit = limit
            for i in range(len(weights)):
                if curLimit - weights[i] < 0:
                    day += 1
                    curLimit = limit
                curLimit -= weights[i]
            if day > days:
                l = limit + 1
            else:
                r = limit - 1
                output = limit
        return output



        