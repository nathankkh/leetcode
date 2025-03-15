from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = [0 for _ in range(len(nums))]

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        houses[0] = nums[0]
        houses[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            houses[i] = max(nums[i] + houses[i-2], houses[i-1])
        return houses[-1]
    
    def robWithLessSpace(self, nums: List[int]) -> int:

        prev_2 = nums[0]
        prev_1 = max(nums[0], nums[1])
        curr = prev_1
        for i in range(2, len(nums)):
            curr = max(prev_2 + nums[i], prev_1)
            prev_2 = prev_1
            prev_1 = curr
        return curr

