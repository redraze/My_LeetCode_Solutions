# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or x < -100 or x > 100:
            return head

        cursor = head
        while cursor:
            if cursor.val < x:
                try:
                    before.next = ListNode(cursor.val)
                    before = before.next
                except NameError:
                    before = ListNode(cursor.val)
                    beforeSentry = before
            else: # head.val > x
                try:
                    after.next = ListNode(cursor.val)
                    after = after.next
                except NameError:
                    after = ListNode(cursor.val)
                    afterSentry = after
            cursor = cursor.next

        try:
            before, after
        except NameError:
            return head
    
        before.next = afterSentry
        return beforeSentry
