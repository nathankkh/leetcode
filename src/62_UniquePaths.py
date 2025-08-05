class Solution:
    # memoised - store the results of all the subproblems (so far 
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        
        def inner(curr_m, curr_n):
            if (curr_m, curr_n) in memo:
                return memo[(curr_m, curr_n)]

            if curr_m == m and curr_n == n:  # if reached dest
                return 1

            # out of bounds
            if curr_m > m or curr_n > n:
                return 0

            res = inner(curr_m, curr_n + 1) + inner(curr_m + 1, curr_n)
            memo[(curr_m, curr_n)] = res
            return res

        return inner(1, 1)
    

    # tabulation
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n
        for _ in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1]+dp[j]
        
        return dp[-1]
    
    # tabulation space optimised
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n
        for _ in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1]+dp[j]
        
        return dp[-1]