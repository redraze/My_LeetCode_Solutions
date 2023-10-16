# solution 1: build a relational graph, then BFS with a stack
# O(n^2) time and space complexity (I think?)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for val, (x, y) in zip(values, equations):
            graph[x][y] = val
            graph[y][x] = 1 / val

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
