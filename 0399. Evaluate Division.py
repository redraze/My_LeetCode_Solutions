# overall O(n^2) time and space complexity
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph of variable relations
        # O(n) time and O(n^2) space complexity
        graph = {}
        for val, (var1, var2) in zip(values, equations):
            if var1 not in graph:
                graph[var1] = {}
            if var2 not in graph:
                graph[var2] = {}
            graph[var1][var2] = val
            graph[var2][var1] = 1 / val

        # O(n^2) time and O(n) space complexity
        ans = []
        for q1, q2 in queries:
            found = False
            stack = [(q1, 1)]
            seen = set()
            while stack:
                var, prod = stack.pop()
                if var in seen or var not in graph:
                    continue
                seen.add(var)
                if var == q2:
                    ans.append(prod)
                    found = True
                    break
                for key, value in graph[var].items():
                    stack.append((key, prod * value))
            if not found:
                ans.append(-1)
                
        return ans
