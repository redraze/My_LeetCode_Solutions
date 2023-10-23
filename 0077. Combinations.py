# my most recent solution: iteration
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        q = deque([
            [num] for num in range(1, n + 1) if n - num >= k - 1
        ])

        for i in range(k - 2, -1, -1):
            for __ in range(len(q)):
                base = q.popleft()
                for j in range(base[-1] + 1, n + 1 - i):
                    temp = base.copy()
                    temp.append(j)
                    q.append(temp)

        return list(q)

# # my first, older solution: recursion
# class Solution:
#     def combine(self, n: int, k: int, r=0) -> List[List[int]]:
#         if k == 1:
#             return [[i] for i in range(1,n+1)]
#         List = []
#         for L in self.combine(n-1, k-1, r+1):
#             for j in range(L[-1]+1,n+1):
#                 List.append(L + [j])
#             k += 1
#         return List
