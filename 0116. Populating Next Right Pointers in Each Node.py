# Use the previously set root.next to bridge the logarithmicly 
# growing gap between the two branches of the root, and each 
# gap in the two branches of the original root's two branches,
# (and so on...) as described in the third conditional statement
# of Solution 1:            root.right.next = root.next.left
# and the second conditional statement in the while
# loop of Solution 2:       cur.right.next = cur.next.left
#
#   Graphically:
#  
#          (root)--------.next-------->(root.next)
#              \                       /
#             .right     (gap)      .left
#                \                   /
#        (root.right)----.next---->(root.right.next = root.next.left)

# Solution 1
# recursion
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return
        if root.right == None:
            return root
        if root.next != None:                                 #   HERE
            root.right.next = root.next.left                  #   <---
        root.left.next = root.right
        root.right = self.connect(root.right)
        root.left = self.connect(root.left)
        return root

    
# Solution 2
# interation with stack 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return
        stack = [root]
        while stack != []:
            cur = stack.pop()
            if cur.left == None:
                continue
            cur.left.next = cur.right
            if cur.next != None:
                cur.right.next = cur.next.left
            stack.append(cur.left)
            stack.append(cur.right)
        return root
