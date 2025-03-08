import math
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def is_prime(num):
            if num == 1:
                return False
            if num == 2 or num == 3:
                return True
            if num%2 == 0:
                return False
            
            to_check = math.floor(num**0.5) + 1
            for i in range(3, to_check + 1, 2):
                if num % i == 0:
                    return False
            return True
        n = min(math.floor((left-1)/6), math.floor((left-5)/6))
        searchable=[]    
        if left<=2<=right:
            searchable.append(2)
        if left<=3<=right:
            searchable.append(3)
        while True:
            x,y = 6*n-1, 6*n+1
            if x > right:
                break
            if right >= x >= left:
                searchable.append(x)
            if right >= y >= left:
                searchable.append(y)
            n+=1
        if len(searchable)<2:
            return[-1,-1]
        # prev = -1
        # min_diff =math.inf
        a,b = -1,-1

        primes = []
        for val in searchable:

            if val < 1 or not is_prime(val):
                continue
            
            # if prev ==-1:
            #     prev = val
            #     a=val
            # else:
            #     print([prev, val])
            #     if val-prev < min_diff:
            #         min_diff = val-prev
            #         a=prev
            #         b=val
            #         prev=val
            primes.append(val)
        if len(primes)  < 2:
            return [-1,-1]
        min_diff = math.inf
        for i in range(len(primes) - 1):
            diff = primes[i+1] - primes[i]
            if diff <= 2:
                return [primes[i], primes[i+1]]
            if diff < min_diff:
                min_diff = diff
                a,b = primes[i], primes[i+1]

        return [a,b]
        
    def sieve(self, left, right):
        arr = [1 for _ in range(right + 2)]
        arr[0] = arr[1] = 0
        i = 2
        
        # for i in range(len(arr)): # naive implementation
        for i in range(2, math.floor(math.sqrt(right)) + 1):
            if arr[i]:
                for j in range(i * i, right + 1, i): 
                    arr[j] = 0
        
        primes = [i for i in range(left, right + 1) if arr[i]]
        min_d, a, b = math.inf, -1, -1
        if len(primes) < 2:
            return [-1,-1]
        for i in range(len(primes)-1):
            diff = primes[i+1] - primes[i]
            if diff <= 2:
                return [primes[i], primes[i+1]]
            if diff < min_d:
                min_d = diff
                a, b = primes[i], primes[i+1]
        return [a,b]
    
sol = Solution()
print(sol.closestPrimes(4,6))
print(sol.sieve(4,6))
