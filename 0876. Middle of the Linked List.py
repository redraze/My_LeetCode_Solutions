# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # two pointer solution
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, j = (head, head)
        index = 0
        while j != None:
            if index%2 != 0:
                i = i.next
                j = j.next
            else:
                j = j.next
            index += 1
        return i
