class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        need to s

        """

        n = len(days)
        
        memo = {}

        def nxt(i, L):
            j = i
            while j < n and days[j] < days[i] + L:
                j += 1
            return j

        def dp(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]

            result = min(costs[0] + dp (nxt(i,1)), costs[1] + dp(nxt(i,7)), costs[2] + dp(nxt(i,30)))

            memo[i] = result
            return result

        return dp(0)