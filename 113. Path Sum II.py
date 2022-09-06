# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # check for empty tree
        if root == None:
            return []
        
        # build all possible paths
        paths = [[]]
        self.buildPaths(root, paths, 0)
        
        # check path sums
        ans = []
        for path in paths:
            if (
                sum(path) == targetSum
            ):
                ans.append(path)
        return ans
    
    def buildPaths(self, root, paths, depth):
        paths[-1].append(root.val)
        if root.left != None:
            self.buildPaths(root.left, paths, depth+1)
        if root.right != None:
            if root.left != None:
                paths.append(paths[-1][0:depth+1])
                self.buildPaths(root.right, paths, depth+1)
            else:
                self.buildPaths(root.right, paths, depth+1)
        return
