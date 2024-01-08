# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time and space complexity
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque([root])
        ret = 0

        while q:
            node = q.popleft()

            if not node:
                continue

            if low <= node.val <= high:
                ret += node.val

            q.append(node.left)
            q.append(node.right)

        return ret
