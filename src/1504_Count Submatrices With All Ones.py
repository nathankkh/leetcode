from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])

        # stores the height of the rectangle that ends at the specified index (assume that everything is 1 col first)
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]:
                    dp[i+1][j+1] = 1+ dp[i][j+1]

        # iterate through each row
        # for each col in the current row, look leftward to count the number of potential subarrays
        res=0
        for i in range(1,r+1):
            count = 0
            curr_row = dp[i]
            for j in range(1, c+1):
                min_h = curr_row[j]
                for k in range(j, 0, -1):
                    # expand leftward to count the number of subarrays that include the jth elem of the current row
                    min_h = min(min_h, curr_row[k])
                    count += min_h
            res += count
        return res