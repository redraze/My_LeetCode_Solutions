class Solution:
    # my most recent solution
    # O(log n) time and O(1) space complexity
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        if not nums or target < nums[0] or target > nums[-1]:
            return ans

        # locate lower boundary
        L, R = 0, len(nums)
        while L < R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L = mid + 1
            else:
                R = mid

        if nums[L] != target:
            return ans
        ans[0] = L

        # locate upper boundary
        L, R = ans[0] + 1, len(nums)
        while L < R:
            mid = (L + R) // 2
            if nums[mid] < target + 1:
                L = mid + 1
            else:
                R = mid
        ans[1] = L - 1

        return ans
    
    # # previous solution
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     # edge cases
    #     if (
    #         nums == [] 
    #         or nums[0] > target 
    #         or nums[-1] < target
    #     ):        
    #         return [-1,-1]
        
    #     # Step 1: trim the sides
    #     L, R = 0, len(nums)-1
    #     while True:
    #         # target not in nums
    #         if L > R:
    #             return [-1,-1]
    #         mid = L + (R-L)//2
    #         if nums[mid] == target:
    #             break
    #         if nums[mid] > target:
    #             R = mid - 1
    #             continue
    #         if nums[mid] < target:
    #             L = mid + 1
    #             continue
        
    #     # Step 2: calibrate left marker
    #     prev = mid
    #     while True:
    #         if nums[L] == target:
    #             break
    #         midL = L + (prev-L)//2
    #         if nums[midL] < target:
    #             L = midL + 1
    #             continue
    #         prev = midL
                
    #     # Step 3: calibrate right marker
    #     while True:
    #         if nums[R] == target:
    #             break
    #         midR = mid + (R-mid)//2
    #         if nums[midR] > target:
    #             R = midR - 1
    #             continue
    #         if nums[midR + 1] != target:
    #             R = midR
    #             break
    #         mid = midR
        
    #     return [L,R]
