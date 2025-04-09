import math
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d=set()
        for i in range(len(nums) -1 , -1, -1):
            a = nums[i]
            if a in d: # this is the place that needs to be sliced
                return math.ceil((i+1)/3)
            else:
                d.add(a)
        return 0