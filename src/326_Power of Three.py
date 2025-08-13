import math

class Solution:

    # recursive
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <3:
            return False
            
        if n % 3 != 0:
            return False
        
        return self.isPowerOfThree(n//3)
    
    # calculate the largest possible int that is a power of 3. 
    # if that value has no remainder when divided by n, it is a power of 3. (since n * unknown number of 3s will eventually reach max value, while
    # another multiple of 3 that is not a power of 3 will not)
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <3:
            return False
            
        # intuition: repeatedly dividing by 3 should have no remainder
        # find largest n using log
        exact_power = math.log((2**31 - 1),3)
        power = int(exact_power)
        max_val = 3**power

        return max_val%n ==0
    
    # iterative - generate all powers of 3 up to the constraint and check if n is present in any one of them
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <3:
            return False
            
        curr=1
        for i in range(1,31):
            curr *=3
            if curr == n:
                return True
        return False