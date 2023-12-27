class Solution:
    # O(n) time and O(1) space complexity
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        timeSpent = 0
        prev = 0
        currentColor = colors[0]

        for i, color in zip(range(1, len(colors)), colors[1:]):
            if color != currentColor:
                if i - prev > 1:
                    timeSpent += sum(neededTime[prev:i]) - max(neededTime[prev:i])
                prev = i
                currentColor = color

        if len(colors) - prev > 1:
            timeSpent += sum(neededTime[prev:]) - max(neededTime[prev:])

        return timeSpent
