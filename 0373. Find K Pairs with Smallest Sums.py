# solution 3: using the heapq module
# O(k log n) time and O(n + k) space complexity,
# where k is the number of pairs requested, and n is len(nums1)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = [[val + nums2[0], i, 0] for i, val in enumerate(nums1)]
        heapq.heapify(q)

        ans = []
        for _ in range(k):
            if not q:
                return ans

            __, i, j = heapq.heappop(q)

            ans.append(
                [
                    nums1[i], 
                    nums2[j]
                ]
            )

            if j + 1 < len(nums2):
                heapq.heappush(
                    q, 
                    [
                        nums1[i] + nums2[j + 1], 
                        i, 
                        j + 1
                    ]
                )

        return ans


# # solution 2: custom heap
# # O(k log n) time and O(n + k) space complexity,
# # where k is the number of pairs requested, and n is len(nums1)
# class Solution:
#     def heapify(self, heap: List[int], nums1: List[int], nums2: List[int], init=False) -> List[int]:
#         if init:
#             stack = list(range(len(heap)//2))
#         else:
#             stack = [0]

#         while stack:
#             idx = stack.pop()
#             heapStatus = self.checkheap(heap, nums1, nums2, idx)

#             if heapStatus:
#                 headVal, leftVal, rightVal = heapStatus
#                 L, R = idx * 2 + 1, idx * 2 + 2

#                 # leaf node
#                 if leftVal == rightVal == None:
#                     continue

#                 elif leftVal == None:
#                     heap[idx], heap[R] = heap[R], heap[idx]
#                     stack.append(R)

#                 elif rightVal == None:
#                     heap[idx], heap[L] = heap[L], heap[idx]
#                     stack.append(L)

#                 elif leftVal < rightVal:
#                     heap[idx], heap[L] = heap[L], heap[idx]
#                     stack.append(L)

#                 else: # leftVal > rightVal:
#                     heap[idx], heap[R] = heap[R], heap[idx]
#                     stack.append(R)

#         return heap
#     def checkheap(self, heap: List[int], nums1: List[int], nums2: List[int], idx: int) -> Optional[List[int]]:
#         try:
#             x, y = heap[idx]
#             headVal = nums1[x] + nums2[y]
#         except IndexError:
#             headVal = None

#         try:
#             x, y = heap[idx * 2 + 1]
#             leftVal = nums1[x] + nums2[y]
#         except IndexError:
#             leftVal = None

#         try:
#             x, y = heap[idx * 2 + 2]
#             rightVal = nums1[x] + nums2[y]
#         except IndexError:
#             rightVal = None

#         if headVal == None or (leftVal != None and leftVal < headVal) or (rightVal != None and rightVal < headVal):
#             return [headVal, leftVal, rightVal]

#         return None
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         heap = [[i, 0] for i in range(len(nums1))]
#         heap = self.heapify(heap, nums1, nums2, init=True)

#         ans = []
#         for _ in range(k):
#             x, y = heap[0]
#             try:
#                 ans.append([nums1[x], nums2[y]])
#             except IndexError:
#                 return ans

#             heap[0][1] += 1
#             self.heapify(heap, nums1, nums2)

#         return ans


# # solution 1: two pointers approach -- TLE
# # O(k * n) time and O(n) space complexity
# class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     refs = [0] * len(nums1)
    #     ans = []

    #     for _ in range(min(k, len(nums1) * len(nums2))):
    #         minPair = [None, float('inf')]

    #         for i, val1 in enumerate(nums1):
    #             try:
    #                 val2 = nums2[refs[i]]
    #                 pairSum = val1 + val2
    #                 if pairSum < minPair[1]:
    #                     minPair = [i, pairSum]
    #             except IndexError:
    #                 pass
            
    #         ans.append([
    #             nums1[minPair[0]],
    #             nums2[refs[minPair[0]]]
    #         ])

    #         refs[minPair[0]] += 1

    #     return ans
