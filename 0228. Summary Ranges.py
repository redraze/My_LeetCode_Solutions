class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # attempt #1
        if nums == []:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]

        L = 0
        ans = []
        for R in range(1, len(nums)):
            if nums[R - 1] != nums[R] - 1:
                if L == R - 1:
                    ans.append(str(nums[L]))
                else:
                    ans.append(
                        '->'.join([
                            str(nums[L]), 
                            str(nums[R - 1])
                        ])
                    )
                L = R

        if L == R:
            ans.append(str(nums[L]))
        else:
            ans.append(
                '->'.join([
                    str(nums[L]), 
                    str(nums[R])
                ])
            )
        return ans
