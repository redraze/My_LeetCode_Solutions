class Solution:
    # min-heap with minimized extra memory usage
    # O(n log k) time with O(k) space complexity
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0]

    # # in-place min-heap using heapq.heapify
    # # O(n log n) time and O(1) space complexity
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heapq.heapify(nums)
    #     for _ in range(len(nums) - k):
    #         heapq.heappop(nums)
    #     return nums[0]
