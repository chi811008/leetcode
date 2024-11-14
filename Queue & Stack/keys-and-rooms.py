from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque()
        q.append(0)

        while q:
            roomNum = q.popleft()
            if roomNum in visited:
                continue
            visited.add(roomNum)
            for key in rooms[roomNum]:
                q.append(key)

        return len(visited) == len(rooms)
