# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftDepth(self, root: Optional[TreeNode], depth=0) -> int:
        while root:
            depth += 1
            root = root.left
        return depth
    def rightDepth(self, root: Optional[TreeNode], depth=0) -> int:
        while root:
            depth += 1
            root = root.right
        return depth
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left = self.leftDepth(root)
        right = self.rightDepth(root)
        if left == right:
            return 2**left - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
