# Use the previously set root.next to bridge the logarithmicly 
# growing gap between the two branches of the root, and each 
# gap in the two branches of the original root's two branches,
# (and so on...) as described in the third conditional statement:
#
#           root.right.next = root.next.left
#
#          (root)--------.next-------->(root.next)
#              \                       /
#             .right     (gap)      .left
#                \                   /
#        (root.right)----.next---->(root.right.next = root.next.left)


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
