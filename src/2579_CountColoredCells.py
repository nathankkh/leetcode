class Solution:
    def coloredCells(self, n: int) -> int:
        if n ==1:
            return 1
        res=1
        for i in range(1,n):
            res += i*4
        return res
    
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return (2*(n**2)) - 2*n + 1