from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # fruits; quantity of the ith type of fruit
        # baskets: capacity of the jth basket
        # iterate through `fruits` and place them in the left-most available basket that has a capacity >= quantity of fruit type
        # return the number of fruits that cannot be placed in any basket
        # 
        res = 0
        n = len(baskets)
        for fruit in fruits:
            flag = False
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0 # set basket as used
                    flag = True
                    break
            if not flag:
                res += 1
        return res