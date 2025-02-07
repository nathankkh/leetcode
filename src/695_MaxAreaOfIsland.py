from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        visited = [[False]* cols for _ in grid]
        largest_area = 0

        def helper(row, col):
            for direction in directions:
                new_r, new_c = row + direction[0], col + direction[1]

                # check bounds
                if rows > new_r >= 0 and cols > new_c >= 0 and not visited[new_r][new_c] and grid[new_r][new_c] == 1:
                    visited[new_r][new_c] = True
                    curr_area[0] += 1
                    helper(new_r,new_c)


        for i in range(rows):
            for j in range(cols):
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if grid[i][j] == 1:
                    curr_area = [1]
                    helper(i, j)
                    largest_area = max(largest_area, curr_area[0])


        return largest_area