# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ivalIdx = {val: i for i, val in enumerate(inorder)}
        def dp(preorder, inorder):
            if not preorder:
                return None
            i = inorder.index(preorder[0])
            return TreeNode(
                preorder[0],
                dp(preorder[1:i + 1], inorder[0:i]),
                dp(preorder[i + 1::], inorder[i + 1::])
            )
        return dp(preorder, inorder)
