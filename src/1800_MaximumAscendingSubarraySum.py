from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        
        curr_subarray, res = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_subarray += nums[i]
            else:
                curr_subarray = nums[i]
            
            res = max(res, curr_subarray)

        return res