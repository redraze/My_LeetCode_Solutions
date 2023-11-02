class Solution:
    # my most recent solution -- tabulation
    # O(m * n) time and O(n) space complexity,
    # where m is avg length of row and n is num rows
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tab = triangle[-1]
        for row in range(len(triangle) - 2, -1, -1):
            for i, val in enumerate(triangle[row]):
                tab[i] = val + min(tab[i], tab[i + 1])
            tab.pop()
        return tab[0]

    # # my previous solutions
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     # Solution 2:
    #     # bottom-up iteration
    #     ans = triangle[-1][:]
    #     for row in triangle[0:-1][::-1]:
    #         for i,x in enumerate(row):
    #             ans[i] = row[i] + min(ans[i], ans[i+1])
    #     return ans[0]
        
    #     '''
    #     # Solution 1:
    #     # recursion with memoization
    #     @cache
    #     def f(depth, position):
    #         if depth == len(triangle) - 1:
    #             mem[depth, position] = triangle[depth][position]
    #             return triangle[depth][position]
    #         return min([
    #             triangle[depth][position] + f(depth+1, position),
    #             triangle[depth][position] + f(depth+1, position+1)
    #         ])
    #     return f(0,0)
    #     '''
