# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # solution #2 -- two pointers
        fast = head
        for i in range(n):
            fast = fast.next

        if not fast:
            head = head.next
            return head

        slow = prev = head
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next
        return head

        # # solution #1 -- recursion
        # if head == None:
        #     return 1
        # temp = self.removeNthFromEnd(head.next, n)
        # if isinstance(temp, int) == True:
        #     if temp == n:
        #         return head.next
        #     return 1 + temp
        # # modify current list
        # head.next = temp
        # return head
        # # create new list to preserve input
        # # return ListNode(head.val, temp)
