from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        return number of subarrays where score < k

        score given by sum(elements) * len(elements)

        values are all positive
        '''

        left = 0
        res = 0
        running = 0
        for right in range(len(nums)):
            running += nums[right]
            check = running * (right - left + 1)
            while check >= k and left <= right:
                running -= nums[left]
                left += 1
                check = running * (right - left + 1)
            
            # all subarrays that begin at/after left are valid
            res += (right - left + 1)
        return res