# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([
            [root, 0]
        ])
        ans = []
        
        # my second solution
        while q:
            [node, depth] = q.popleft()
            if not node:
                continue
            q.append([node.left, depth + 1])
            q.append([node.right, depth + 1])
            try:
                if depth % 2:
                    ans[depth] = [node.val] + ans[depth]
                else:
                    ans[depth].append(node.val)
            except IndexError:
                ans.append([node.val])
        return ans

        # # My first solution
        # while q:
        #     [node, depth] = q.popleft()
        #     if not node:
        #         continue
        #     q.append([node.left, depth + 1])
        #     q.append([node.right, depth + 1])
        #     try:
        #         ans[depth].append(node.val)
        #     except IndexError:
        #         ans.append([node.val])
        
        # switch = False
        # for i in range(len(ans)):
        #     if switch:
        #         ans[i].reverse()
        #     switch = not switch
        # return ans
