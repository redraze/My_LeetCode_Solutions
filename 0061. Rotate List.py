# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head

        # I think the extra O(n) runtime to find the length of the 
        # list is worth it, since k >>> len(head) is a possibility 
        length = 0
        cursor = head
        while cursor:
            cursor = cursor.next
            length += 1

        k %= length
        if k == 0:
            return head

        cursor = head
        for i in range(length - k):
            prev = cursor
            cursor = cursor.next
        prev.next = None
        sentry = cursor

        while cursor.next:
            cursor = cursor.next
        cursor.next = head

        return sentry
