class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        for i, num in enumerate(arr):
            if num != arr[i - 1]:
                count = 1
            else:
                count += 1
            if count > len(arr) / 4:
                return num
        return arr[-1]
