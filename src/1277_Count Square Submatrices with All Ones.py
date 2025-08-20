from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # m x n matrix of 1s and 0s 
        # return number of square submatrices that are all 1s
        res = 0
        # single variables count as square subarrays
        r = len(matrix)
        c = len(matrix[0])

        res = 0
        dp = [[0] * (c + 1) for _ in range(r+1)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    res+= dp[i+1][j+1]

        return res
        


tc = [ 
    ([[0,1,1,1],[1,1,1,1],[0,1,1,1]], 15), 
    ([[1,0,1],[1,1,0],[1,1,0]],7) 
]

sol = Solution()
for t, a in tc:
    print(sol.countSquares(t) == a)
