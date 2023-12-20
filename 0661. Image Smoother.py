class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        w, h = len(img[0]), len(img)

        def findAverage(r: int, c: int, sum: int, count = 1) -> int:
            dirs = [
                [1, 0],     # up
                [-1, 0],    # down
                [0, 1],     # right
                [0, -1],    # left
                [1, 1],     # up right
                [1, -1],    # up left
                [-1, 1],    # down right
                [-1, -1]    # down, left
            ]

            for dr, dc in dirs:
                if 0 <= (r + dr) < h and 0 <= (c + dc) < w:
                    count += 1
                    sum += img[r + dr][c + dc]

            return int(sum / count)

        ret = []
        for i, row in enumerate(img):
            ret.append([])
            for j, num in enumerate(row):
                ret[-1].append(findAverage(i, j, num))

        return ret
