class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        i, j, k = 0, len(nums) - 1, 0
        while i != j:
            if nums[i] != val:
                k += 1
                i += 1
            else:
                while nums[j] == val:
                    if i == j:
                        return k
                    j -= 1
                nums[i] = nums[j]
                nums[j] = val
                j -= 1
        if nums[i] != val:
            k += 1
        return k
