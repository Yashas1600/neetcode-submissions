class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """

        """
        memo = {}
        ROWS = len(triangle)
        def dp(row, i):
            if row == ROWS:
                return 0
            if (row, i) in memo:
                return memo[(row,i)]
            result = triangle[row][i] + min(dp(row+1, i), dp(row + 1, i +1))
            memo[(row,i)] = result
            return result
        return dp(0,0)

        

        