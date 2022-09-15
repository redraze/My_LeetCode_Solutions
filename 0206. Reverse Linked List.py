# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 3
# Recursion (with memory magic)
class Solution:
    def reverseList(self, head: Optional[ListNode], index=0) -> Optional[ListNode]:
        # PART 1: recurse to the end of 'head'.
        # returns the last node of 'head' to the 
        # second to last recursion
        print(f'recursion level = {index}, head ID = {id(head)}, head = {head}')
        if not head or not head.next:
            print('\n\tBOTTOM RECURSION LEVEL REACHED')
            print(f'\n----------recursion level: {index}-----------------')
            print(f'head ID = {id(head)}')
            if head:
                print(f'head.next ID = {id(head.next)}')
            print(f'head = {head}')
            if head:
                print(f'head.next = {head.next}')
            return head
        # Part 2: finish out each recursion.
        # retrieve the reverse of head.next
        # (ie: the part of the linked list that 
        # remains after cutting off it's head)
        node = self.reverseList(head.next,index+1)
        # the variable 'node' refers to the same place in physical memory 
        # as the last listnode of the unmutated linked list 'head'
        print(f'\n----------recursion level: {index}-----------------')
        print('\n\tSTEP 1: after setting node:')
        print(f'head ID = {id(head)}')
        print(f'head.next ID = {id(head.next)}')
        print(f'head.next.next ID = {id(head.next.next)}')
        print(f'node ID = {id(node)}')
        print(f'node.next ID = {id(node.next)}')
        print(f'head = {head}')
        print(f'node = {node}')
        # point the last listnode in 'node' to the first listnode in the current 
        # recursion's version of 'head'. the last listnode in 'node' can be accessed 
        # through 'head' since some of the listnodes of both 'node' and 'head' share 
        # the same locations in memory. this makes 'head' into an infinite loop 
        # (and also creates an infinite loop at the end of 'node') because, again, 
        # some of the listnodes of 'node' and 'head' share the same locations in memory.
        head.next.next = head
        # 
        # For example: 
        # in loop level 3, just after 'node' has been pointed to the physical 
        # location in memory of the last listnode in 'head':
        # node = 5 -> None
        # head = 4 -> 5 -> None
        #
        # we could use 'node.next' to set the last listnode of 'head' to 
        # point to the first listnode of 'head', but we wouldn't be able to 
        # do this if node = 5 -> 4 -> 3 -> 2
        #
        # thus, we use head.next.next to access the pointer of the last listnode 
        # in 'head', thus creating the infinite loops:
        # node = 5 -> 4 -> 5 -> ...
        # head = 4 -> 5 -> 4 -> ...
        #
        # we want node = 5 -> 4 -> None
        # but how do we access the "last" listnode in 'node'?
        # (I say "last" because there is no last listnode in 'node' anymore)
        #
        # We can access the "last" listnode of 'node' through 'head'
        # since the first listnode in 'head' shares the same memory location
        # of the "last" listnode of 'node'
        print('\n\tSTEP 2: after setting head.next.next = head:')
        print(f'head ID = {id(head)}')
        print(f'head.next ID = {id(head.next)}')
        print(f'head.next.next ID = {id(head.next.next)}')
        print(f'node ID = {id(node)}')
        print(f'node.next ID = {id(node.next)}')
        print(f'head = {head}')
        print(f'node = {node}')
        head.next = None
        # continuing the previous example: now,
        # head = 4 -> None
        # node = 5 -> head
        # or
        # node = 5 -> 4 -> None
        print('\n\tSTEP 3: after setting head.next = None:')
        print(f'head ID = {id(head)}')
        print(f'head.next ID = {id(head.next)}')
        print(f'node ID = {id(node)}')
        print(f'node.next ID = {id(node.next)}')
        print(f'head = {head}')
        print(f'node = {node}')
        # finally, pass the reversed section of 'head' back up the recursion chain
        return node
        
        
'''
# Solution 2
# Iteration only
# Preserves input
# Runtime O(n)
# Space complexity O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
'''

'''
# Soltuion 1
# Stack and iteration
# Preserves input
# Overall runtime O(n)
# Space complexity O(n)
from collections import deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create stack with all values from list
        # Runtime O(n)
        stack = deque()
        temp = head
        while temp != None:
            stack.append(temp.val)
            temp = temp.next
                
        # Iteratevly pop stack while building new linked list
        # Runtime O(n)
        if stack:
            ans = ListNode(stack.popleft())
            while stack:
                temp = ListNode(stack.popleft())
                temp.next = ans
                ans = temp
            return ans
        return
'''
