from typing import List
from collections import deque


# if the 2D grid's value == 0: land block
# any other value means that the area on the grid is a water block. The value represents the number of fishes on that block
# Find the max number of fish that the fisherman can get, assuming he starts from an optimal position
# the fisherman cannot step on land
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        num_r = len(grid)
        num_c = len(grid[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        res = 0
        for i in range(num_r):
            for j in range(num_c):
                if grid[i][j] != 0:
                    stack = [[i, j]]
                    curr = grid[i][j]
                    grid[i][j] = 0
                    while stack:
                        r, c = stack.pop()
                        for d in directions:
                            new_r = r + d[0]
                            new_c = c + d[1]
                            if (
                                0 <= new_r < num_r
                                and 0 <= new_c < num_c
                                and grid[new_r][new_c] != 0
                            ):
                                curr += grid[new_r][new_c]
                                grid[new_r][new_c] = 0
                                stack.append([new_r, new_c])
                    if curr > res:
                        res = curr
        return res


sol = Solution()
grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
sol.findMaxFish(grid)
