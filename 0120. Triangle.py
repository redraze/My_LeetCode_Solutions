class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def f(depth, position):
            if depth == len(triangle) - 1:
                return triangle[depth][position]
            return min([
                triangle[depth][position] + f(depth+1, position),
                triangle[depth][position] + f(depth+1, position+1)
            ])
        return f(0,0)
