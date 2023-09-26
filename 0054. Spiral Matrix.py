class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        width, height = len(matrix[0]), len(matrix)
        size = width * height

        seen = set()
        seen.add((0,0))

        x, y = 0, 0
        ans = [matrix[0][0]]
        counter = 1

        #         right    down     left     up
        offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while True:
            for (i, j) in offset:
                
                if counter == size:
                    return ans

                while (
                    (x + i, y + j) not in seen
                    and 0 <= x + i < width
                    and 0 <= y + j < height
                ):
                    x, y = x + i, y + j
                    
                    seen.add((x, y))
                    ans.append(matrix[y][x])
                    counter += 1

        return ans
