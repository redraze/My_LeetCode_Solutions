class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # edge cases
        if (
            nums == [] 
            or nums[0] > target 
            or nums[-1] < target
        ):        
            return [-1,-1]
        
        # Step 1: trim the sides
        L, R = 0, len(nums)-1
        while True:
            # target not in nums
            if L > R:
                return [-1,-1]
            mid = L + (R-L)//2
            if nums[mid] == target:
                break
            if nums[mid] > target:
                R = mid - 1
                continue
            if nums[mid] < target:
                L = mid + 1
                continue
        
        # Step 2: calibrate left marker
        prev = mid
        while True:
            if nums[L] == target:
                break
            midL = L + (prev-L)//2
            if nums[midL] < target:
                L = midL + 1
                continue
            prev = midL
                
        # Step 3: calibrate right marker
        while True:
            if nums[R] == target:
                break
            midR = mid + (R-mid)//2
            if nums[midR] > target:
                R = midR - 1
                continue
            if nums[midR + 1] != target:
                R = midR
                break
            mid = midR
        
        return [L,R]
