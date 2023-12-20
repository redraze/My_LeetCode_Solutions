class Solution:
    # O(m * n) time and space complexity
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        h, w = len(img), len(img[0])

        rng = range(-1, 2)
        def findAverage(r: int, c: int, sum = 0, count = 0) -> int:
            for dr in rng:
                for dc in rng:
                    if 0 <= (r + dr) < h and 0 <= (c + dc) < w:
                        count += 1
                        sum += img[r + dr][c + dc]

            return int(sum / count)

        return [[findAverage(r, c) for c in range(w)] for r in range(h)]
