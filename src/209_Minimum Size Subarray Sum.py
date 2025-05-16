import math
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return the minimum length of a subarray whose sum is greater than or equal to target
        if nums[0] >= target:
            return 1
        if len(nums) == 1:
            return 0
        left,right=0,1
        n = len(nums)
        curr_sum = nums[0]
        res = math.inf
        
        while right < len(nums):
            curr_sum += nums[right]

            while curr_sum >= target:
                if right == left: 
                    res = 1
                else:
                    res = min((right - left + 1), res)
                curr_sum -= nums[left]
                left += 1

            right += 1
        if res == math.inf:
            return 0
        else: 
            return res

target = 7
nums=[2,3,1,2,4,3]
sol = Solution()
sol.minSubArrayLen(target, nums)