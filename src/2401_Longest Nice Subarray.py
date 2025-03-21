from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 1
        res = 1
        res_temp = 1
        curr = nums[left]
        while right < len(nums) :

            if curr & nums[right] == 0:
                res_temp += 1
                curr = curr | nums[right]
                res = max(res_temp, res)
                right += 1
            else:
                while left < right and curr & nums[right] != 0:
                    curr ^= nums[left]
                    left += 1
                    res_temp -=1
                
        return res