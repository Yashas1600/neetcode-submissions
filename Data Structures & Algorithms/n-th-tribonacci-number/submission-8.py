class Solution:
    def tribonacci(self, n: int) -> int:
        #T(0) 
        first = 0
        second = 1
        third = 1
        if n <= 2:
            return [0, 1, 1][n]
        i = 3
        res= 0
        while i <= n:
            res = first + second + third
            first = second
            second = third
            third = res
            i += 1
        return res
            


