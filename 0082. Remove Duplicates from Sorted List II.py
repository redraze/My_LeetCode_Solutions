class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not head:
            return None
        if (
            head.next != None
            and head.val == head.next.val
        ):
            return self.deleteDuplicates(head.next, head.val)
        if head.val == prev:
            return self.deleteDuplicates(head.next, prev)
        head.next = self.deleteDuplicates(head.next, head.val)
        return head
