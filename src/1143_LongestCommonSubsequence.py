class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Subsequence: 
        Without changing the order of letters, delete any number of characters at any position to form a subsequence

        e.g. abcd -> a, b, c, d, ad, ac ...
        '''
        if not text1 or not text2:
            return 0
        # create a 2d memo of text1+1 rows, text2+1 cols
        num_rows = len(text1) + 1
        num_cols = len(text2) + 1

        dp = [[0] * num_cols for _ in range(num_rows)]

        for i in range(1,num_rows):
            for j in range(1,num_cols):
                # check if letters are the same
                # if they are, take the previous value and + 1

                # else make curr dp position max(upper_val, left_val)
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # bottom right corner is the ans
        return dp[num_rows-1][num_cols-1]
    
s1='aytx'
s2='ax'
print(Solution().longestCommonSubsequence(s1,s2))

