# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solution 2
    # O(n * k) time complexity and O(k) space complexity,
    # where n is len(list) and k is total number of nodes
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [L for L in lists if L]
        ans = cur = ListNode()
        while lists:
            # find index of list with the smallest node value in lists
            minVal = min(lists, key=lambda x: x.val)
            for i, L in enumerate(lists):
                if L.val == minVal.val:
                    idx = i
                    break

            cur.next = lists[idx]
            cur = cur.next
            lists[idx] = lists[idx].next

            if not lists[idx]:
                lists.pop(idx)

        return ans.next


    # # solution 1
    # # using a dictionary of index: lists entries
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     d = {key: val for key, val in zip(range(len(lists)), lists) if val}
    #     ans = cur = ListNode()

    #     while d:
    #         key = min(d, key=lambda x: d[x].val)
    #         cur.next = d[key]
    #         cur = cur.next
    #         d[key] = d[key].next
    #         if not d[key]:
    #             del d[key]

    #     return ans.next
