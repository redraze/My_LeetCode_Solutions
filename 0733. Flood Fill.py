class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, targetColor: int) -> List[List[int]]:
        # image is already effectively flood-filled
        if image[sr][sc] == targetColor:
            return image
        
        sourceColor = image[sr][sc]
        image[sr][sc] = targetColor
        visited = set()
        visited.add(
            (sr,sc)
        )
        image = self.flood(image, sr, sc, targetColor, sourceColor, visited)
        return image
    
    def flood(self, image, sr, sc, targetColor, sourceColor, visited):
        directions = [
            (sr-1,sc),
            (sr+1,sc),
            (sr,sc-1),
            (sr,sc+1)
        ]
        for d in directions:
            if (
                d not in visited
                and d[0] < len(image) and d[0] >= 0
                and d[1] < len(image[0]) and d[1] >= 0
                and image[d[0]][d[1]] == sourceColor 
            ):
                image[d[0]][d[1]] = targetColor
                visited.add(
                    d
                )
                self.flood(image, d[0], d[1], targetColor, sourceColor, visited)
        return image
