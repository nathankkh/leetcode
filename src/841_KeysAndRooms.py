from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in rooms]
        stack = [0]
        count = 0
        while len(stack) > 0:
            curr_room_idx = stack.pop()
            if visited[curr_room_idx]:
                continue
            visited[curr_room_idx] = True
            count += 1
            # append all childre
            stack.extend(rooms[curr_room_idx])
        return count == len(rooms)

