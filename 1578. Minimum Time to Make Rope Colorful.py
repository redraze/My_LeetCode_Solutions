# Another solution
# O(n) time and O(1) space complexity
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        timeSpent = 0
        prevIdx = 0
        prevColor = colors[0]
        sumTimeNeeded, maxTimeNeeded = 0, neededTime[0]

        for i, [color, time] in zip(
            range(1, len(colors)), 
            zip(
                colors[1:],
                neededTime[1:]
                )
            ):

            if color != prevColor:
                if i - prevIdx > 1:
                    timeSpent += sumTimeNeeded
                prevIdx = i
                prevColor = color
                sumTimeNeeded, maxTimeNeeded = 0, time

            else:
                sumTimeNeeded += min(maxTimeNeeded, time)
                maxTimeNeeded = max(maxTimeNeeded, time)

        if len(colors) - prevIdx > 1:
            return timeSpent + sumTimeNeeded
        return timeSpent

# # My first solution:
# # O(n) time and O(1) space complexity
# class Solution:
#     def minCost(self, colors: str, neededTime: List[int]) -> int:
#         timeSpent = 0
#         prev = 0
#         currentColor = colors[0]

#         for i, color in zip(range(1, len(colors)), colors[1:]):
#             if color != currentColor:
#                 if i - prev > 1:
#                     timeSpent += sum(neededTime[prev:i]) - max(neededTime[prev:i])
#                 prev = i
#                 currentColor = color

#         if len(colors) - prev > 1:
#             timeSpent += sum(neededTime[prev:]) - max(neededTime[prev:])

#         return timeSpent
