class Solution:
    # O(n) time and space complexity
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        ret = [[]]

        for num in nums:
            row = seen.get(num, 0)
            seen[num] = row + 1

            if row >= len(ret):
                ret.append([num])
            else:
                ret[row].append(num)

        return ret
