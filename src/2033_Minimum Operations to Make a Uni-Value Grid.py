from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        remainder = grid[0][0] % x
        temp = []
        for row in grid:
            for col in row:
                if col%x != remainder:
                    return -1
                temp.append(col)
        temp.sort()
        target = temp[len(temp) // 2]

        count = 0
        for t in temp:
#            print(f'current val: {t}. {abs(t-target)}')
            count += abs(t - target) // x
            
        return count
        
print('tc1')
x=1
grid=[[1,5],[2,3]]
sol = Solution()
sol.minOperations(grid, x)