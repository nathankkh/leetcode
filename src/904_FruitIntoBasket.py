from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)

        if n == 1:
            return 1
        
        left = 0
        res = -1
        d = {fruits[0]: 1}
        curr = 1
        for right in range(1, n):
            if fruits[right] in d:
                d[fruits[right]] += 1
                curr += 1
            else:
                if len(d) == 1:
                    d[fruits[right]] = 1
                    curr += 1
                    continue

                # update res
                if curr > res:
                    res = curr

                # shift leftward until either element in d == 0
                # decrement curr
                while True:
                    d[fruits[left]]-=1
                    curr -= 1
                    # terminating condition
                    if d[fruits[left]] == 0:
                        del d[fruits[left]]
                        left += 1
                        break
                    left += 1
                
                # add in the new set of fruits
                d[fruits[right]] = 1
                curr += 1

        return max(res, curr)
            

# less verbose
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <= 2:
            return n

        left = 0
        res = 0
        d={}

        for right in range(n):
            d[fruits[right]] = d.get(fruits[right], 0) + 1
            
            while len(d) > 2:
                # shift left pointer
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1    
            if (right - left + 1) > res:
                res = (right - left + 1)
        return res

