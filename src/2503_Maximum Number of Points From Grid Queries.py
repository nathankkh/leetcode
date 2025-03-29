from typing import List
from collections import deque

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        Given a 2d array grid
        given a 1d array queries
        return a 1d array answers

        Start from top left of a grid and move outwards, if the query value > grid value

        """

        d = {k: -1 for k in queries}

        for i in range(len(queries)):
            if d[queries[i]] == -1:
                val = self.helper(grid, queries[i])
                d[queries[i]] = val
            queries[i] = d[queries[i]]
        return queries

    def helper(self, grid, val):
        if grid[0][0] > val:
            return 0
        visited = [[False for _ in grid[0]] for _ in grid]
        max_r = len(grid) - 1
        max_c = len(grid[0]) - 1

        queue = deque()
        score = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue.append((0, 0))
        visited[0][0] = True
        while queue:
            curr_r, curr_c = queue.popleft()

            if grid[curr_r][curr_c] >= val :
                continue
            else:
                score += 1

                for dir in directions:
                    new_r = curr_r + dir[0]
                    new_c = curr_c + dir[1]

                    if new_r >= 0 and new_r <= max_r and new_c >= 0 and new_c <= max_c:
                        if not visited[new_r][new_c]:
                            visited[new_r][new_c] = True
                            queue.append((new_r, new_c))
        return score
    

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted(set(queries))
        query_to_result = {query: 0 for query in queries}

        queue = deque


grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
expected = [5, 8, 1]
sol = Solution()
sol.maxPoints(grid, queries)
