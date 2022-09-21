class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        ans = []
        while i < len(A) and j < len(B):
            Amin, Bmin = A[i][0], B[j][0]
            Amax, Bmax = A[i][-1], B[j][-1]
            if (
                (Amax >= Bmin and Amin <= Bmax)
                or (Bmin <= Amax and Bmax >= Amin)
            ): 
                ans.append([
                        max(Amin, Bmin),
                        min(Amax, Bmax)
                ])
            if Amax < Bmax:
                i += 1
                continue
            j += 1
        return ans
