from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        
        capacity = nums[0]
        idx = 0
        n = len(nums) - 1
        while capacity >= 0:
            if idx == n:
                return True
            
            capacity -= 1
            if capacity < 0:
                return False
            idx += 1
            capacity = max(capacity, nums[idx])
        return False
    
sol = Solution()
sol.canJump([2,0,0])