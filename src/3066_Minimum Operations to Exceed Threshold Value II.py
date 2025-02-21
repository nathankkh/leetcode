from typing import List
from heapq import heapify
from heapq import heappop, heappush

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        '''
        Take 2 smallest integers from nums
        Remove them
        Add min(x,y) * 2 + max(x,y) 
        Return min operations such that all elems >= k
        '''
        res = 0
        heapify(nums) #O(n)
        while len(nums) >=2:
            x=heappop(nums)
            if x >= k:
                break
            y=heappop(nums)
            heappush(nums, (x*2 + y))
            res += 1
        return res
        