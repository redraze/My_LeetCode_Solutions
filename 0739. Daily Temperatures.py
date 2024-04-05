# O(n) time and space algorithm
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = n * [0]
        stack = []
        
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]

            while stack:
                if stack[-1][0] > temp:
                    break
                stack.pop()

            if len(stack) == 0:
                ret[i] = 0
            else:
                ret[i] = stack[-1][1] - i

            stack.append((temp, i))

        return ret
