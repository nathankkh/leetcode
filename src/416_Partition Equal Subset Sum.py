from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [[False]*(target+1) for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            dp[i][0] = True

        # dp[i][j] shows whether, as at the ith element, the sum j can be met
        for i in range(1,len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i-1] <= j: # either take or skip
                    # is current value valid? take j (required sum) - nums[i-1] (because it is 1-indexed rn) -> if resuult is true, then current value(nums[i-1]) will contribute to the sum
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]] # can sum(i-1 elems) = j - nums[i-1]
                else: # current num > sum required, can only skip
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

