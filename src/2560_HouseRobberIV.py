import math
from typing import List

class Solution:
    def minCapability(self, nums:List[int], k:int) -> int:
        ''' 
        If the robber must steal from at least k houses,
        find the minimum X, where X represents the house with the highest value out of all houses robbed
        '''
        def helper(val):
            # val refers to the required value
            # can you rob at least k houses, where all the houses are <= val?
            count = 0
            i=0
            while i < len(nums):
                if nums[i] <= val:
                    count += 1
                    i += 2
                    if count == k:
                        return True
                else:
                    i += 1
            return count >= k

        min_val = min(nums)
        max_val = max(nums)

        while min_val < max_val:
            mid = ((max_val - min_val) // 2) + min_val
            if helper(mid): # reduce 
                max_val = mid
            else:
                min_val = mid + 1
        return min_val
    
    
    def minCapabilityWrong(self, nums: List[int], k: int) -> int:
        '''
        constraints: k is such that there is always a valid ans

        2d dp
        Each row (i) represents a house
        Each col (j) represents the number of houses robbed so far
        dp[i][j] represents the amount robbed when the robber is at the ith house, having robbed j houses
        '''
        dp = [[math.inf]*(k+1) for _ in range(len(nums))]

        # handle base cases
        for i in range(len(nums)):
            dp[i][0] = 0
        dp[0][1] = nums[0]
        
        for i in range(1, len(nums)):
        
            for j in range(1,k+1):
                # either skip -take previous row's result
                dp[i][j] = dp[i-1][j]

                # or take(if possible)
                if i >= 1 and j >= 1:
                    if i >= 2:
                        prev = dp[i-2][j-1]
                    else:
                        prev = 0 if j == 1 else math.inf
                    dp[i][j] = min(dp[i][j], prev+nums[i])
        
            print(dp)
        return dp[-1][-1]

test = [2,3,5,9]
k=2
sol = Solution()
sol.minCapability(test, k)



'''
Given k houses to rob, find the minimum amount robbed
'''