# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None

        ans = ListNode()
        ansCursor = ans
        headCursor = head

        # deep copy entire head input without reversing any section
        if left == right:
            ans = ListNode()
            ansCursor = ans
            headCursor = head
            while headCursor.next:
                ansCursor.val = headCursor.val
                headCursor = headCursor.next
                ansCursor.next = ListNode()
                ansCursor = ansCursor.next
            ansCursor.val = headCursor.val
            return ans

        # deep copy head list up to node before left index
        i = 1
        while i < left:
            ansCursor.val = headCursor.val
            headCursor = headCursor.next
            i += 1
            if i == left:
                break
            ansCursor.next = ListNode()
            ansCursor = ansCursor.next

        # made a reversed deep copy of the section of the 
        # head list between the left and right markers
        reversedListEnd = ListNode()
        revCursor = reversedListEnd
        revCursor.val = headCursor.val
        while i < right:
            headCursor = headCursor.next
            temp = ListNode(headCursor.val)
            temp.next = revCursor
            revCursor = temp
            i += 1
        headCursor = headCursor.next

        # attach the reversed section to the end of the beginning section
        if left == 1:
            ans = revCursor
        else:
            ansCursor.next = revCursor

        # deep copy the rest of the head list beyond the right marker
        ansCursor = reversedListEnd
        while headCursor:
            ansCursor.next = ListNode(headCursor.val)
            ansCursor = ansCursor.next
            headCursor = headCursor.next

        return ans
