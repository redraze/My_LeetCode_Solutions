"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def findNext_2(self, cursor: 'Node') -> ['Node' , 'Node']:
        if not cursor:
            return [None, None]
        if cursor.left:
            return [cursor.left, cursor]
        if cursor.right:
            return [cursor.right, cursor]
        return self.findNext(cursor.next)

    # iterative solution [O(1) space effeciency]
    def connect(self, root: 'Node') -> 'Node':
        cursor, dummy = root, None
        while cursor != dummy:
            while cursor:
                if cursor.left:
                    if not dummy:
                        dummy = cursor.left
                    if cursor.right:
                        cursor.left.next = cursor.right
                    else:
                        cursor.left.next, cursor = self.findNext_2(cursor.next)
                        continue

                if cursor.right:
                    if not dummy:
                        dummy = cursor.right
                    cursor.right.next, cursor = self.findNext_2(cursor.next)
                    continue

                cursor = cursor.next

            if dummy:
                cursor, dummy = dummy, None
        return root


    # def findNext(self, prev: 'Node') -> 'Node':
    #     if not prev:
    #         return None
    #     if prev.left:
    #         return prev.left
    #     if prev.right:
    #         return prev.right
    #     return self.findNext(prev.next)

    # # iterative solution [O(n) space effeciency]
    # def connect(self, root: 'Node') -> 'Node':
        # from collections import deque
        # q = deque()
        # q.append(root)
        # while q:
        #     node = q.popleft()
        #     if not node:
        #         continue

        #     if node.right:
        #         node.right.next = self.findNext(node.next)
        #         q.append(node.right)

        #     if node.left:
        #         if node.right:
        #             node.left.next = node.right
        #         else:
        #             node.left.next = self.findNext(node.next)
        #         q.append(node.left)

        # return root

    # # recursive solution
    # def connect(self, root: 'Node') -> 'Node':
        # if not root:
        #     return None

        # if root.right:
        #     root.right.next = self.findNext(root.next)

        # if root.left:
        #     if root.right:
        #         root.left.next = root.right
        #     else:
        #         root.left.next = self.findNext(root.next)

        # self.connect(root.right)
        # self.connect(root.left)
        # return root
