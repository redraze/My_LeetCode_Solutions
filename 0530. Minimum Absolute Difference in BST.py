# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solution #2: inorder traversal
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        diff = 10 * 10 * 10 * 10 * 10
        prev = 10 * 10 * 10 * 10 * 10 * -1
        stack, cursor = [], root
        while cursor or stack:
            while cursor:
                stack.append(cursor)
                cursor = cursor.left
            node = stack.pop()
            diff = min(diff, node.val - prev)
            prev, cursor = node.val, node.right
        return diff

    # # solution 1: walk the tree and complile a sorted list
    # # O(n log n) time and O(n) space complexity
    # def __init__(self) -> None:
    #     self.set = set()
    #     return
    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #     self.dp(root)
    #     diff = 10 * 10 * 10 * 10 * 10
    #     sortedList = sorted(list(self.set))
    #     for i, val in enumerate(sortedList):
    #         try:
    #             diff = min(
    #                 sortedList[i + 1] - val,
    #                 diff
    #             )
    #         except IndexError:
    #             pass
    #     return diff
    # def dp(self, node: Optional[TreeNode]) -> None:
    #     if not node:
    #         return 
    #     self.set.add(node.val)
    #     self.dp(node.left)
    #     self.dp(node.right)
    #     return
