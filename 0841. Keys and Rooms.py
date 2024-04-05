# O(n) time space complexity
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visit and pick up keys from first room
        visited = set([0])
        stack = rooms[0]

        while stack:
            room = stack.pop()

            if room in visited:
                continue

            visited.add(room)

            for key in rooms[room]:
                stack.append(key)

        if len(visited) == len(rooms):
            return True
        return False
