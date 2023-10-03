class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        count = 1
        prev = points[0][1]
        for point in points[1::]:
            if prev >= point[0]:
                prev = min(prev, point[1])
            else:
                count += 1
                prev = point[1]
        return count
