# Runtime O(n)
# Sapce Complexity O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        sentry = prev = Node()
        sentry.next = root
		# depth search
        while root:
            prev = root
			# breadth search
            while root:
                if root.left:
                    if root.right:
                        root.left.next = root.right
                        root.right.next = self.findChild(root.next)
                    else:
                        root.left.next = self.findChild(root.next)
                if root.right:
                    root.right.next = self.findChild(root.next)
                root = root.next
            if prev.left:
                root = prev.left
                continue
            if prev.right:
                root = prev.right
                continue
            root = prev.next
        return sentry.next
        
	# searches horizontally for next node with a child to point to.
	# called when there are missing child nodes between parent nodes
    def findChild(self, root):
        if not root:
            return
        if root.left:
            return root.left
        if root.right:
            return root.right
        return self.findChild(root.next)
