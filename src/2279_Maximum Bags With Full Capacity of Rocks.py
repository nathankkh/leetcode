from typing import List
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # greedy impl

        for r in range(len(capacity)):
            capacity[r] -= rocks[r]
        capacity.sort()

        for i, b in enumerate(capacity):
            if b > additionalRocks:
                return i
            else:
                additionalRocks -= b
        return i+1
    
capacity = [2,3,4,5]
rocks=[1,2,4,4]
additionalRocks = 2
sol = Solution()
sol.maximumBags(capacity, rocks, additionalRocks)