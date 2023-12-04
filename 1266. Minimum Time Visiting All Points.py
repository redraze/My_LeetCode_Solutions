class Solution:
    # one-liner :p
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(
            max(
                abs(points[i][0] - points[i + 1][0]),
                abs(points[i][1] - points[i + 1][1])
            ) for i in range(len(points) - 1)
        )
    
    # # O(n) time and O(1) space complexity
    # def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    #     time = 0

    #     for i, point in enumerate(points[:-1]):
    #         time += max([
    #             abs(point[0] - points[i + 1][0]),
    #             abs(point[1] - points[i + 1][1])
    #         ])

    #     return time
