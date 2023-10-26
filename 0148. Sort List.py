# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next

        nodes = sorted(nodes, key=lambda x: x.val)
        nodes.append(None)

        for i, node in enumerate(nodes[:len(nodes) - 1]):
            node.next = nodes[i + 1]

        return nodes[0]
