class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if n < 2 or n % 2 != 0:
                continue
            
            mid = n // 2
            if sum(int(x) for x in s[:mid]) == sum(int(x) for x in s[mid:]):
                count += 1
        return count
    
left=1200
right = 1230
sol = Solution()
sol.countSymmetricIntegers(left, right)