from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a = -1
        b = -1
        n = len(grid)
        for row in grid:
            for col in row:
                if col in seen:
                    a=col
                else:
                    seen.add(col)
        
        for i in range(1,n**n + 1):
            if i in seen:
                continue
            else:
                b=i
                break
        return [a,b]
    
    
tests = [ [[1,3],[2,2]], [[9,1,7],[8,9,2],[3,4,6]], [[1,3,4],[9,7,5],[8,2,3]]]
ans = [[2,4], [9,5], [3,6]]
sol = Solution()
for i in range(len(tests)):
    print(i, ': ', sol.findMissingAndRepeatedValues(tests[i]) == ans[i])