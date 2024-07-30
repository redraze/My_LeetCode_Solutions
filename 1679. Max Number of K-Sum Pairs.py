class Solution:
    # # two pointer on a sorted array
    # # O(n log n) time and O(1) space complexity
    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     nums = sorted(nums)
    #     L, R = 0, len(nums) - 1
    #     out = 0

    #     while L < R:
    #         sum = nums[L] + nums[R]
    #         if sum == k:
    #             out += 1
    #             L += 1
    #             R -= 1
    #         elif sum > k:
    #             R -= 1
    #         else: #sum < k
    #             L += 1

    #     return out

    # hash table solution
    # O(n) space and time complexity
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        out = 0

        for num in nums:
            d[num] += 1
            comp = k - num

            if num == comp:
                if d[num] > 1:
                    out += 1
                    d[num] -= 2

            elif d[num] > 0 and comp in d and d[comp] > 0:
                out += 1
                d[num] -= 1
                d[comp] -= 1

        return out
