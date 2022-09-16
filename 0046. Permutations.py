class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # returns a list of the input list 
        # if the input list only contains one number
        if len(nums) < 2:
            return [nums]
        List = []
        # iterate through each item in the input list...
        for i, num in enumerate(nums):
            # and append that item with each possible permutation of the 
            # remainder of the input list
            for j in self.permute(nums[0:i] + nums[i+1::]):
                # store each of those items + permute appends in another list
                # to be either returned to the top level call
                # or passed up the recursion chain
                List.append([nums[i]] + j)
        return List
