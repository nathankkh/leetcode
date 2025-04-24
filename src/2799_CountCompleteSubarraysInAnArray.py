from typing import List
from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
      
        l=0
        distinct = len(set(nums))
        res=0
        inner_seen = defaultdict(int)
        
        for r in range(len(nums)):
            inner_seen[nums[r]] += 1
            
            while len(inner_seen) == distinct:
                res += len(nums) - r
                inner_seen[nums[l]] -= 1

                if inner_seen[nums[l]] == 0:
                    del inner_seen[nums[l]]

                l+= 1

        return res
            