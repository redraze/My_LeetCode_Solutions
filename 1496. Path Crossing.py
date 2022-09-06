class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # keep set of visited locations
        visited = {(0,0)}
        place = [0,0]
        
        # iterate through path
        for d in path:
            if d == 'N':
                place[1] += 1
            elif d == 'S':
                place[1] -= 1
            elif d == 'E':
                place[0] += 1
            else:   # d == 'W'
                place[0] -= 1
            # check to see if new place has already been visited
            if tuple(place) in visited:
                return True
            else:
                visited.add((tuple(place)))
            
        # path does not cross
        print(visited)
        return False
