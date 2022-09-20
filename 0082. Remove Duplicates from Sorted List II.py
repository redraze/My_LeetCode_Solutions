class Solution:
    # Solution 2:
    # iteration
    # O(n) runtime
    # O(1) space complexity
    def deleteDuplicates(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        pointer = ListNode(0, head)
        prev = pointer
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
                continue
            head = head.next
            prev = prev.next
        return pointer.next
    
    '''
    # Solution 1:
    # recursion
    # O(n) runtime
    # O(n) space complexity
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
    '''
