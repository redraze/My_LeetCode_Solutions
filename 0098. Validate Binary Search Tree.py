# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # solution 3: inorder traversal (recursion)
        # O(n) time and O(n) space complexity
        def dp(node: Optional[TreeNode], lowerLimit: int, upperLimit: int) -> bool:
            if node.left:
                dp(node.left, lowerLimit, node.val)
            if not self.ans or node.val <= lowerLimit or node.val >= upperLimit:
                self.ans = False
                return
            if node.right:
                dp(node.right, node.val, upperLimit)
            return
        self.ans = True
        dp(root, -2**31 - 1, 2**31 + 1)
        return self.ans


        # # solution 2: inorder traversal (stack)
        # # O(n) time and O(n) space complexity
        # stack = []
        # cursor = root
        # prev = -2**31 - 1
        # while stack or cursor:
        #     while cursor:
        #         stack.append(cursor)
        #         cursor = cursor.left
        #     cursor = stack.pop()
        #     if cursor.val <= prev:
        #         return False
        #     prev = cursor.val
        #     cursor = cursor.right
        # return True


        # # solution 1: recursive tree walk with inherited value limits
        # # O(n) time and O(n) space complexity
        # def dp(root: Optional[TreeNode], lowerLimit: int, upperLimit: int) -> bool:
        #     if not root:
        #         return True
        #     if (
        #         root.val <= lowerLimit
        #         or root.val >= upperLimit
        #     ):
        #         return False
        #     return (
        #         dp(root.left, lowerLimit, root.val)
        #         and dp(root.right, root.val, upperLimit)
        #     )
        # return dp(root, -2**31 - 1, 2**31 + 1)
