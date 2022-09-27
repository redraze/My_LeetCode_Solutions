# Flood fill
# Runtime O(n^2)
# Space complexity O(n)
class Solution:
    from collections import deque
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        visited = set()
        toMove = deque()
        toMove.append((0,0))
        distance = 0
        n = len(grid)-1
        while toMove:
            for i in range(len(toMove)):
                pos = toMove.popleft()
                visited.add((pos))
                moves = [
                    (pos[0]+1,pos[1]),
                    (pos[0]+1,pos[1]+1),
                    (pos[0],pos[1]+1),
                    (pos[0]-1,pos[1]+1),
                    (pos[0]-1,pos[1]),
                    (pos[0]-1,pos[1]-1),
                    (pos[0],pos[1]-1),
                    (pos[0]+1,pos[1]-1)
                ]
                for move in moves:
                    if (
                        (move[0],move[1]) not in visited
                        and (move[0],move[1]) not in toMove
                        and 0 <= move[0] <= n
                        and 0 <= move[1] <= n
                        and grid[move[0]][move[1]] != 1
                    ):
                        toMove.append((move[0],move[1]))
            distance += 1
            if (n,n) in visited:
                return distance
        return -1
