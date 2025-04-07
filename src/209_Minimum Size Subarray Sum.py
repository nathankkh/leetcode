from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return the minimum length of a subarray whose sum is greater than or equal to target
        if nums[0] >= target:
            return True
        if len(nums) == 1:
            return False
        left,right=0,1
        n = len(nums)
        curr_sum = nums[0]
        res = 0
        if curr_sum >= target:
            return 1
        while right < n:
            # expand until target is reached, shrink left
            while curr_sum >= target:
                if not res:
                    res = right - left
                else:
                    res = min(res, right - left)
                curr_sum -= nums[left]
                left += 1
            curr_sum += nums[right]
            right += 1
        return res
target = 7
nums=[2,3,1,2,4,3]
sol = Solution()
sol.minSubArrayLen(target, nums)