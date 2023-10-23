class Solution:
    # my third solution -- iteration
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cLen = len(candidates)

        stack = [ [[], 0, 0] ]
        while stack:
            [path, i, sum] = stack.pop()

            if sum == target:
                ans.append(path)
                continue
            if i == cLen or sum > target:
                continue

            while i < cLen:
                stack.append((path + [candidates[i]], i, sum + candidates[i]))
                i += 1

        return ans

    # # my second solution -- recursion
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     sortedNums = sorted(candidates)
    #     ans = []
    #     def dp(path: List[int], nums: List[int], sum: int) -> None:
    #         if sum == target:
    #             ans.append(path)
    #             return
    #         if not nums or sum > target:
    #             return
    #         for i, num in enumerate(nums):
    #             dp(path + [num], nums[i:], sum + num)
    #         return
    #     dp([], candidates, 0)
    #     return ans

    # # my first solution -- TLE
    # # (I think it works?)
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     def dp(path: List[int], nums: List[int], target: int) -> None:
    #         if not nums:
    #             return
    #         for i, val in enumerate(nums):
    #             if not target % val:
    #                 ansAppend(sorted(
    #                     path + [val] * int(target / val)
    #                 ))

    #             sliced = nums[:i] + nums[i + 1:]
    #             count = 0
    #             while target - (val * count) > 0:
    #                 dp(path + ([val] * count), sliced, target - (val * count))
    #                 count += 1
    #         return

    #     def ansAppend(nums: List[int]) -> None:
    #         s = ''.join([str(val) for val in nums])
    #         if s not in ans:
    #             ans[s] = nums
    #         return

    #     ans = defaultdict()
    #     dp([], candidates, target)
    #     return [val for val in ans.values()]
