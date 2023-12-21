class Solution:
    # O(n log n) time and O(1 space) complexity
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])

        ret = 0
        for i in range(1, len(points)):
            diff = points[i][0] - points[i - 1][0]
            ret = max(ret, diff)

        return ret
