class Solution:
    # solution 2: tabulation with binary search
    # O(n log n) time and O(n) space complexity
    def lengthOfLIS(self, nums: List[int]) -> int:
        tab = [nums[0]]

        for num in nums[1:]:
            if num > tab[-1]:
                tab.append(num)
            else:
                # using my custom bin search
                L, R = 0, len(tab)
                while L != R:
                    mid = (L + R) // 2
                    if tab[mid] >= num:
                        R = mid
                    else:
                        L = mid + 1
                try:
                    tab[L] = num
                except IndexError:
                    tab[-1] = num

                # # using the bisect module
                # idx = bisect.bisect_left(tab, num)
                # tab[idx] = num

        return len(tab)


    # # solution 1: tabulation
    # # O(n^2) time and O(n) space complexity
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     ans, tab = 1, [1] * len(nums)
    #     for i in range(len(nums)):
    #         for j in range(0, i):
    #             if nums[j] < nums[i]:
    #                 tab[i] = max(tab[i], tab[j] + 1)
    #                 ans = max(ans, tab[i])
    #     return ans
