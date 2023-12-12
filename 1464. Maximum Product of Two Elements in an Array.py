class Solution:
    # solution 1: heap
    # O(n) time and O(1) space complexity
    def maxProduct(self, nums: List[int]) -> int:
        heap = nums[:2]
        heapq.heapify(heap)

        for num in nums[2:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        return (heap[0] - 1) * (heap[1] - 1)
