# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # empty tree
        if root == None:
            return False

        # leaf reached
        if (
            (
                root.left == root.right == None
                and targetSum - root.val == 0
            )
        ):
            return True

        # continue with depth first search
        if (
            self.hasPathSum(root.right, targetSum - root.val)
            or
            self.hasPathSum(root.left, targetSum - root.val)
        ):
            return True
        return False
