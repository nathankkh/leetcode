from collections import deque
from typing import List
import math

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        queue = deque()
        timeTaken = [[math.inf] * cols for _ in grid]
        freshOranges = 0
        maxTime = 0
        # Traverse grid and add all rotten oranges to queue/array
        # isfresh array -> visited array?
        # for each orange, bfs
        
        # populate queue with rotten oranges
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    # add rotten oranges to queue
                    queue.append((row, col))
                    # set the timeTaken to reach rotten oranges as 0
                    timeTaken[row][col] = 0
                # check for islands for early termination
                elif grid[row][col] == 1:
                    freshOranges+= 1
                    isIsland = True
                    for direction in directions:
                        new_row, new_col = row + direction[0], col + direction[1]
                        if rows > new_row >= 0 and cols > new_col >= 0 and grid[new_row][new_col] != 0:
                            isIsland = False
                            break
                    if isIsland:
                        # print('early termination')
                        return -1
        
        # for each item in queue
        while queue:
            curr_row, curr_col = queue.popleft()

            for direction in directions:
                new_row, new_col = curr_row + direction[0], curr_col + direction[1]
                # ensure neighbour is not visited AND is a fresh orange
                if rows > new_row >= 0 and cols > new_col >= 0 and timeTaken[new_row][new_col] == math.inf and grid[new_row][new_col] == 1:
                    freshOranges-= 1
                    queue.append((new_row, new_col))
                    timeTaken[new_row][new_col] = timeTaken[curr_row][curr_col] + 1
                    maxTime = max(maxTime, timeTaken[curr_row][curr_col] + 1)
                
        # return the time taken for all fresh oranges to be reached
        if freshOranges:
            return -1
        else:
            return maxTime

sol = Solution()
print('test 1')
grid = [[2,1,1],[1,1,0],[0,1,1]]
print( sol.orangesRotting(grid) )

print('test 2')
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(sol.orangesRotting(grid))

print('test 3')
grid = [[0,2]]
print(sol.orangesRotting(grid))