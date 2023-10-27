class Solution:
    # most recent solution -- iteration
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1

        # target is outside of matrix boundaries
        if target < matrix[0][0] or target > matrix[m][n]:
            return False

        # identify row that should contain target
        L, R = 0, m
        while L < R:
            mid = (L + R) // 2
            if matrix[mid][-1] < target:
                L = mid + 1
            else:
                R = mid
        row = matrix[L]

        # target is outside of row boundaries
        if target < row[0] or target > row[-1]:
            return False

        # identify index where target should be
        L, R = 0, n
        while L < R:
            mid = (L + R) // 2
            if row[mid] < target:
                L = mid + 1
            else:
                R = mid

        if row[L] == target:
            return True
        return False



    # # previous solution -- recursion
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     # search for a row that may contain the target
    #     if matrix == []:
    #         return False
    #     m = len(matrix)//2
    #     mid = matrix[m][0]
    #     if target == mid:
    #         return True
    #     if target > mid:
    #         if target > matrix[m][-1]:
    #             return self.searchMatrix(matrix[m+1::], target)
    #         return self.searchRow(matrix[m][1::], target)
    #     return self.searchMatrix(matrix[0:m], target)
        
    # # search the row that may contain the target
    # def searchRow(self, nums, target):
    #     if nums == []:
    #         return False
    #     m = len(nums)//2
    #     mid = nums[m]
    #     if mid == target:
    #         return True
    #     if target < mid:
    #         return self.searchRow(nums[0:m], target)
    #     return self.searchRow(nums[m+1::], target)
