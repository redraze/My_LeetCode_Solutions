# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # empty tree
        if root == None:
            return []
        
        # find all paths. runtime: O(n)
        paths = self.findPaths(root, [[]], 0)
        
        # format paths
        for i, path in enumerate(paths):
            paths[i] = str(path)[1:-1].replace(', ','->')
        return paths
    
    def findPaths(self, root, paths, index):
        if root == None:
            return []
        paths[-1].append(root.val)
        if root.left != None:
            self.findPaths(root.left, paths, index+1)
        if root.right != None:
            if root.left != None:
                paths.append(paths[-1][0:index+1])
                self.findPaths(root.right, paths, index+1)
            else:
                self.findPaths(root.right, paths, index+1)
        return paths
