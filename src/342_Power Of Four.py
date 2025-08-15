import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False
        if n == 1:
            return True
        if n <4:
            return False
        curr = 1
        arr =[1]
        while curr < 2**31-1:
            curr *=4
            arr.append(curr)
        return n in arr
        


tc = [0, 1, -128, 4, 3, 8, 16, 32, 65536,64,5]
ans = [False, True, False, True, False, False, True, False, True, True,False]
sol = Solution()
for i in range(len(tc)):
    print(sol.isPowerOfFour(tc[i]) == ans[i])



