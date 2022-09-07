# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        return int(self.recurse(root, targetSum, 0, 0, False))
            
    def recurse(self, root, targetSum, Sum, depth, copy):
        paths = 0
        Sum += root.val
        if Sum == targetSum:
            paths += 1
        if root.left != None:
            # continue original root sum,
            # and create new copy sum starting from 0 on next node
            if copy == False:
                paths += self.recurse(root.left, targetSum, Sum, depth+1, False)
                paths += self.recurse(root.left, targetSum, 0, depth+1, True)
            # if root copy, only continue copy sum. 
            # do not create new copy sum starting from 0 on next node,
            # as this will be done by original root sum
            else:
                paths += self.recurse(root.left, targetSum, Sum, depth+1, True)
        if root.right != None:
            if copy == True:
                paths += self.recurse(root.right, targetSum, Sum, depth+1, True)
            if copy == False:
                paths += self.recurse(root.right, targetSum, Sum, depth+1, False)
                paths += self.recurse(root.right, targetSum, 0, depth+1, True)
        return paths
