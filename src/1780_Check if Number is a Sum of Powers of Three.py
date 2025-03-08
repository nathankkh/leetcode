class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Given an integer n, return true if it is possible to represent n 
        as the sum of distinct powers of three. Otherwise, return false.

        An integer y is a power of three if there exists an integer x such that y == 3^x.
        1 <= n <= 10^7
        -> this means powers of [0, 14]
        """

        
        def convertBase3(num):
            if num == 0: return '0'
            res = []
            while num > 0:
                res.append(str(num%3))
                num = num // 3
            return (''.join(reversed(res)))
        
        temp = convertBase3(n)
        for i in temp:
            if i == '2':
                return False
        return True
    def checkPowersOfThreeBacktrack(self, n):
        
        def backtrack(curr_power, n):

            if n == 0:
                return True
            if pow(3, curr_power) > n:
                return False
            
            # either take this power or skip this power
            take = backtrack(curr_power + 1, n - pow(3, curr_power))
            skip = backtrack(curr_power + 1, n)
            return take or skip
        
        return backtrack(0, n)
    
sol = Solution()
tests = [12, 91, 21]
ans = [True, True, False]

for i in tests:
    print(sol.checkPowersOfThree(i))

print(sol.checkPowersOfThreeBacktrack(12))