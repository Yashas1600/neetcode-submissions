class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        prices = [7,1,5,3,6,4]
        dp = [float(-"inf")] * len(prices)

        """

        dp = [0] * len(prices)
        dp[0] = 0
        lastBought = 0
        curProfit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i - 1]:
                #buy
                lastBought = i
                dp[i] = curProfit
            #sell
            else:
                
                dp[i] = dp[i-1] + prices[i] - prices[lastBought]
                curProfit = dp[i]
                lastBought = i
        print(dp)
        return dp[len(prices) -1]

    
            
"""
last bought = 6
[0,0,4,4,7,7]
            
curProfit = 7
"""
        