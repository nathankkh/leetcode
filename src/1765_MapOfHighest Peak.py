import math

from collections import deque

class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        numRows = len(isWater)
        numCols = len(isWater[0])
        distance = [[math.inf] * numCols for _ in range(numRows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for i in range(numRows):
            for j in range(numCols):
                if isWater[i][j] == 1:
                    distance[i][j] = 0
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            for drow, dcol in directions:
                new_row, new_col = row + drow, col + dcol
                if 0 <= new_row < numRows and 0 <= new_col < numCols and distance[new_row][new_col] == math.inf:
                    distance[new_row][new_col] = distance[row][col] + 1
                    queue.append((new_row, new_col))

        return distance