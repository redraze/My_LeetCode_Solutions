# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # soultion 2: fast and slow pointers
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

        # # solution #1: using a hash table
        # s = set()
        # while head and head.next != None:
        #     if id(head) in s:
        #         return True
        #     s.add(id(head))
        #     head = head.next
        # return False
