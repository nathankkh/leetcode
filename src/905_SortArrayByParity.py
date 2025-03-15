from collections import deque
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e =[]
        o = []
        for i in nums:
            if i&1 == 0:
                e.append(i)
            else: 
                o.append(i)
        e.extend(o)
        return e
    
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        q=deque()
        for i in nums:
            if i&1 == 0:
                q.appendleft(i)
            else: 
                q.append(i)
        return q