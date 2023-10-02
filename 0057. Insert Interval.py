class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        used = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                out.append(interval)
            elif interval[0] > newInterval[1]:
                if not used:
                    out.append(newInterval)
                    used = True
                out.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]
        if not used:
            out.append(newInterval)
        return out
