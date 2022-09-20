class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # empty array
        if nums == []:
            return -1
        
        # single item array
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        L, R = nums[0], nums[-1]
        m = len(nums)//2
        mid = nums[m]
        
        # target found
        if target == mid:
            return m
        if target == R:
            return len(nums)-1
        if target == L:
            return 0
        
        # ---- REFINE SEARCH ----
        
        # Case 1: nums is unshifted
        if L < R:
            # target not in unshifted nums
            if target > R or target < L:
                return -1
            if target < mid:
                return self.search(nums[0:m], target)                    
            ans = self.search(nums[m+1::], target)
            if ans == -1:
                return -1
            return m + 1 + ans

        # Case 2: nums is shifted
        # target not in shifted nums
        if target < L and target > R:
            return -1
        
        # target is either larger or smaller than all indexes,
        # must base search off of loop location
        if (
            (target > mid and target > R)
            or (target < mid and target < L)
        ):
            # loop on right
            if R < mid:
                ans = self.search(nums[m+1::], target)
                if ans == -1:
                    return -1
                return m + 1 + ans
            # loop on left
            return self.search(nums[0:m], target)                    
        
        # target is not larger or smaller than all indexes
        if target > mid:
            if target < R:
                ans = self.search(nums[m+1::], target)
                if ans == -1:
                    return -1
                return m + 1 + ans
            return self.search(nums[0:m], target)                    
        if target > L:
            return self.search(nums[0:m], target)                    
        ans = self.search(nums[m+1::], target)
        if ans == -1:
            return -1
        return m + 1 + ans
