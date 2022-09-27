class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == sub.val and self.match(root, sub) == True:
            return True
        return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)

    def match(self, root, sub):
        if not root and not sub:
            return True
        if not root or not sub or root.val != sub.val:
            return False
        return self.match(root.left, sub.left) and self.match(root.right, sub.right)
