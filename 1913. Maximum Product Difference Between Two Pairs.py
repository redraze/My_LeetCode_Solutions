class Solution:
    # O(n) time and O(1) space complexity
    def maxProductDifference(self, nums: List[int]) -> int:
        minHeap = sorted(nums[:2])
        maxHeap = minHeap.copy()

        for num in nums[2:]:
            if num > maxHeap[1]:
                maxHeap[0], maxHeap[1] = maxHeap[1], num
            elif num > maxHeap[0]:
                maxHeap[0] = num

            if num < minHeap[0]:
                minHeap[0], minHeap[1] = num, minHeap[0]
            elif num < minHeap[1]:
                minHeap[1] = num

        return (maxHeap[0] * maxHeap[1]) - (minHeap[0] * minHeap[1])

    # # O(n log n) time and O(1) space complexity
    # def maxProductDifference(self, nums: List[int]) -> int:
    #     nums = sorted(nums)
    #     return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
