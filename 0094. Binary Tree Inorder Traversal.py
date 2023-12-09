# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ret = [], []

        def DFS(node):
            while node:
                stack.append(node)
                node = node.left
            return
        
        DFS(root)

        while stack:
            node = stack.pop()
            ret.append(node.val)
            DFS(node.right)

        return ret
