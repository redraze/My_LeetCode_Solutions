class Solution:
    # two passes
    # O(mn) time and O(max(m, n)) space complexity
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = [0] * len(mat)
        c = [0] * len(mat[0])

        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                if num:
                    r[i] += 1
                    c[j] += 1
        
        ans = 0
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                if num and r[i] == 1 and c[j] == 1:
                    ans += 1

        return ans
