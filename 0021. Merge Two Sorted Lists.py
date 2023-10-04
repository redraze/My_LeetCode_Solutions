# my most recent solution
# preserves the original input
# O( max(m, n) ) time and O( max(m, n) ) space complexity
# where m and n are the lengths of list1 and list2, respectively

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        sentry = ListNode()
        cur = sentry
        l1, l2 = list1, list2

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.val = l1.val
                    l1 = l1.next
                else: # l2.val > l1.val
                    cur.val = l2.val
                    l2 = l2.next
            elif not l1:
                cur.val = l2.val
                l2 = l2.next
            else: # not l2
                cur.val = l1.val
                l1 = l1.next
            
            if l1 or l2:
                cur.next = ListNode()
                cur = cur.next

        return sentry

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if list1.val <= list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         list2.next = self.mergeTwoLists(list1, list2.next)
#         return list2
