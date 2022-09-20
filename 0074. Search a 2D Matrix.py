class Solution:
    # search for a row that may contain the target
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        m = len(matrix)//2
        mid = matrix[m][0]
        if target == mid:
            return True
        if target > mid:
            if target > matrix[m][-1]:
                return self.searchMatrix(matrix[m+1::], target)
            return self.searchRow(matrix[m][1::], target)
        return self.searchMatrix(matrix[0:m], target)
        
      # search the row that may contain the target
      def searchRow(self, nums, target):
        if nums == []:
            return False
        m = len(nums)//2
        mid = nums[m]
        if mid == target:
            return True
        if target < mid:
            return self.searchRow(nums[0:m], target)
        return self.searchRow(nums[m+1::], target)
