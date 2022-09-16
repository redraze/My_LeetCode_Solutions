class Solution:
    def combine(self, n: int, k: int, r=0) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1,n+1)]
        List = []
        for L in self.combine(n-1, k-1, r+1):
            for j in range(L[-1]+1,n+1):
                List.append(L + [j])
            k += 1
        return List
