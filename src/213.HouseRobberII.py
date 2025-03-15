import math
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Houses are arranged in a circle
        Cannot rob from adjacent houses
        find max amount of money

        Either 
        '''
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        def helper(arr):
            if len(arr) == 1:
                return arr[0]
            if len(arr) == 2:
                return max(arr)
            twoback = arr[0]
            oneback = max(arr[1], twoback)
            curr = 0
            for i in range(2, len(arr)):
                curr = max(oneback, twoback+arr[i])
                twoback = oneback
                oneback = curr
            return curr
        
        
        # either start from the first house (and ignore the last house) or 
        # start from the second house (and take the last house)
        a = helper(nums[:-1])
        b = helper(nums[1:])
        return max(a,b)