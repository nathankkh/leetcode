import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = array of piles of different sizes
        # h: Total time constraint
        # n log m
        # n: As you iterate through all the different possible piles
        # m: 
        # Base case: h = len(piles)
        slow = 1
        fast = max(piles) # O(n)

        res = fast
        
        while slow <= fast:
            mid_speed = (slow + fast) // 2
            curr_time = 0
            for pile in piles:
                curr_time += math.ceil(pile/mid_speed)

            if curr_time <= h:
                # too fast
                res = mid_speed
                fast = mid_speed - 1
            else:
                # too slow
                slow = mid_speed + 1
        return res

                
'''
If they told you how fast koko was eating, how long does he take to finish all the piles?
> 
If they added a constraint on the time and told you the speed, can he do it within this time?
> 
'''
