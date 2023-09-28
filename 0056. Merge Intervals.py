class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for i, interval in enumerate(
            sorted(
                intervals,
                key=lambda interval: interval[0]
            )
        ):
            if i == 0:
                ans.append(interval)
                continue
            if ans[-1][1] < interval[0]:
                ans.append(interval)
                continue
            if interval[1] > ans[-1][1]:
                ans[-1][1] = interval[1]
        return ans
