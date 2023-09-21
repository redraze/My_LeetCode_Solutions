class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solution 3: like solution 2 but iterate only once
        ret = [1] * len(nums)
        pre, post, j = 1, 1, len(nums) - 1
        for i, val in enumerate(nums):
            ret[i] *= pre
            pre *= val
            ret[j] *= post
            post *= nums[j]
            j -= 1
        return ret

        # # solution 2: keeping track of a product while 
        # # iterating through (twice)
        # ret = [1] * len(nums)
        # # iterate forwards, to multiply each val in ret by 
        # # the product of every val before it's idx in nums
        # product = 1
        # for i, val in enumerate(nums):
        #     ret[i] *= product
        #     product *= val
        # # then iterate backwards, to multiply each val in ret
        # # by the product of every val after it's idx in nums
        # product = 1
        # for i in range(len(nums), 0, -1):
        #     ret[i - 1] *= product
        #     product *= nums[i - 1]            
        # return ret

        # # Initial solution (using division)
        # # Complexity: O(n) time, O(1) space
        # zeroes = 0
        # loc = 0
        # product = 1
        # for i, val in enumerate(nums):
        #     if val == 0:
        #         zeroes += 1
        #         loc = i
        #     else:
        #         product *= val
        # ret = [0] * len(nums)
        # if zeroes == 1:
        #     ret[loc] = product
        #     return ret
        # if zeroes > 1:
        #     return ret

        # for i, val in enumerate(nums):
        #     nums[i] = int(product / val)
        # return nums
