"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node'], prev = None) -> Optional['Node']:
        if not node:
            return None

        stack = [node]
        seen = set()
        d = {}
        while stack:
            node = stack.pop()
            if node.val in seen:
                continue
            seen.add(node.val)

            if node.val not in d:
                d[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor.val not in d:
                    d[neighbor.val] = Node(neighbor.val)
                d[node.val].neighbors.append(d[neighbor.val])
                if neighbor.val not in seen:
                    stack.append(neighbor)        
            
        return d[1]
