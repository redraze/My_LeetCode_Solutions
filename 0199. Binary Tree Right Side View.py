# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([
            [root, 0]
        ])
        while q:
            [node, depth] = q.popleft()
            if not node:
                continue
            q.append([node.left, depth + 1])
            q.append([node.right, depth + 1])
            try:
                ans[depth] = node.val
            except IndexError:
                ans.append(node.val)
        return ans
