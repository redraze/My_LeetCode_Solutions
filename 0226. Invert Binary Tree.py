# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # Recursive solution
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return
    #     root.left, root.right = root.right, root.left
    #     self.invertTree(root.left)
    #     self.invertTree(root.right)
    #     return root

    # Iterative solution w/ stack
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]
        while stack:
            for i in range(len(stack)):
                node = stack.pop()

                if not (node.left or node.right):
                    continue

                node.left, node.right = node.right, node.left

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return root
