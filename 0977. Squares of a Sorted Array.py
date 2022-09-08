class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # runtime O(n)
        L = 0
        R = len(nums) - 1
        ans = []
        while L <= R:
            if abs(nums[L]) < abs(nums[R]):
                ans.append(nums[R]**2)
                R -= 1
                continue
            ans.append(nums[L]**2)
            L += 1
        # reverse answer list, runtime O(n/2).
        # using append (above) and doing this 
        # avoids using python's insert method (which 
        # is O(n) runtime for each insert) which would  
        # increase the overall runtime up to O(n^2)
        L = 0
        while L < int(len(ans)/2):
            R = len(nums) - 1 - L
            ans[L] += ans[R]
            ans[R] = ans[L] - ans[R]
            ans[L] -= ans[R]
            L += 1
        return ans
