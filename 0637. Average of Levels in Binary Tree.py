# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS solution
        q = deque([
            [root, 0]
        ])
        ans = []
        while q:
            [node, depth] = q.popleft()
            if not node:
                continue
            q.append([node.left, depth + 1])
            q.append([node.right, depth + 1])
            try:
                ans[depth]
            except IndexError:
                ans.append([0,0])
            ans[depth][0] += node.val
            ans[depth][1] += 1
        for i, val in enumerate(ans):
            ans[i] = val[0] / val[1]
        return ans

        # # DFS solution
        # ans = []
        # def dp(root, depth=0):
        #     if not root:
        #         return
        #     try:
        #         ans[depth]
        #     except IndexError:
        #         ans.append([0,0])
        #     ans[depth][0] += root.val
        #     ans[depth][1] += 1
        #     dp(root.left, depth + 1)
        #     dp(root.right, depth + 1)
        #     return
        # dp(root)
        # for i, val in enumerate(ans):
        #     ans[i] = val[0] / val[1]
        # return ans
