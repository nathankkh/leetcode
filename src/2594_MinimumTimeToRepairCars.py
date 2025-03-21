from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # x = r * n^2
        # x/r = n^2
        # n = sqrt(x/r)
        def helper(ranks, cars, time):
            count=0
            for r in ranks:
                #n = int( math.pow((time / r), 0.5) )
                count += math.isqrt( (time // r) )
                if count >= cars:
                    return True
            if count < cars:
                return False
        left, right = 0, min(ranks) * (cars**2)


        while left < right:
            mid = (right + left) // 2
            if helper(ranks,cars,mid):
                right = mid
            else:
                left = mid + 1
        return left