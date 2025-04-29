from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        find the max elem of nums
        sliding window to find subarrays that appear *at least* k times
        += len(nums) - r
        '''
        n = len(nums)
        res = 0
        target = max(nums)
        left = 0
        counter = 0
        for right in range(n):
            if nums[right] == target:
                counter += 1
            while counter == k:
                if nums[left] == target:
                    counter -= 1
                left += 1
            res += n - right
        return res
                    

