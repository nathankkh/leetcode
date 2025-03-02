from collections import deque
import math

'''
Explanation
Given a 2D matrix and a starting point, find the distance from the starting point to everywhere else

A specified target can be given as well, but this example will populate a distance[] array

---

Initialise a distance array with infinite distances
Set starting location as 0 in the distance array

Initialise a queue. This queue will hold all future locations to visit
The queue will be populated with the current node's neighbours

Once the queue is empty, all reachable nodes from the start point have been visited. 
Return the distance array
'''


def bfs(startingRow, startingCol, twoDimArray : list[list]) -> list[list]:
    rows, cols = len(twoDimArray), len(twoDimArray[0])
    directions = [(0,1), (1,0), (-1, 0), (0, -1)]
    
    # initialise distance array and set starting distance as 0
    distance = [[math.inf] * cols for _ in twoDimArray]
    distance[startingRow][startingCol] = 0
    
    queue = deque([(startingRow, startingCol)])
    while queue:
        curr_row, curr_col = queue.popleft()

        # add neighbours to list if valid
        for direction in directions:
            # get neighbour's coordinates
            new_row, new_col = curr_row + direction[0], curr_col + direction[1]

            # ensure neighbours are not out of range AND have not been visited before
            if rows > new_row >= 0 and cols > new_col >= 0 and distance[new_row][new_col] == math.inf:
                # add the neighbour to the queue and update the distance array
                queue.append((new_row, new_col))
                distance[new_row][new_col] = min(distance[new_row][new_col], distance[curr_row][curr_col] + 1)

    # once queue is empty, return
    return distance

def test_bfs():
    # Test case 1: Simple 3x3 grid
    grid1 = [
        [0, 0, 0],
        [0, 0, 0], 
        [0, 0, 0]
    ]
    expected1 = [
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4]
    ]
    assert bfs(0, 0, grid1) == expected1, "Test case 1 failed"

    # Test case 2: 4x4 grid starting from middle
    grid2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    expected2 = [
        [2, 1, 2, 3],
        [1, 0, 1, 2],
        [2, 1, 2, 3],
        [3, 2, 3, 4]
    ]
    assert bfs(1, 1, grid2) == expected2, "Test case 2 failed"

    # Test case 3: 2x4 rectangular grid
    grid3 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    expected3 = [
        [1, 2, 3, 4],
        [0, 1, 2, 3]
    ]
    assert bfs(1, 0, grid3) == expected3, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_bfs()

