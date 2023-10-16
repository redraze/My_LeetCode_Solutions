# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solution 3: inorder traversal (recursion)
    # O(k) time and O(n) space complexity
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.ans = False
        def dp(node: Optional[TreeNode]) -> None:
            if not node or self.ans:
                return
            dp(node.left)
            if self.ans:
                return
            self.i += 1
            if self.i == k:
                self.ans = node.val
                return
            dp(node.right)
            return
        dp(root)
        return self.ans


    # # solution 2: inorder traversal (stack)
    # # O(k) time and O(n) space complexity
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     stack = []
    #     cursor = root
    #     i = 0
    #     while stack or cursor:
    #         while cursor:
    #             stack.append(cursor)
    #             cursor = cursor.left
    #         cursor = stack.pop()
    #         i += 1
    #         if i == k:
    #             return cursor.val
    #         cursor = cursor.right
    #     return k


    # # solution 1: tree to sorted list
    # # O(n) time and O(n) space complexity
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     self.set = set()
    #     def treeWalk(node: Optional[TreeNode]) -> None:
    #         if not node:
    #             return
    #         self.set.add(node.val)
    #         treeWalk(node.left)
    #         treeWalk(node.right)
    #         return
    #     treeWalk(root)
    #     return sorted(list(self.set))[k - 1]
