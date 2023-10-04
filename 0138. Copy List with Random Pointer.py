"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # an array containing all the nodes of the deep copy
        nodes = [Node(0)]

        # dictionary containing node id's and index pairs from head input
        # ie:   { '123456789': 0, '11265894': 1, ... }
        ids = {id(None): None}

        # build the deep copy (without random pointers)
        # while keeping track of head id's
        i, cur = 0, head
        while cur:
            ids[id(cur)] = i
            i += 1

            nodes[-1].val = cur.val
            if cur.next:
                nodes[-1].next = Node(0)
                nodes.append(nodes[-1].next)
            cur = cur.next

        # fill in random pointers
        cur = head
        for node in nodes:
            i = ids[id(cur.random)]
            if i != None:
                node.random = nodes[i]
            else:
                node.random = None
            cur = cur.next

        return nodes[0]
