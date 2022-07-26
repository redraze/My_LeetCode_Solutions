###
#
# Haven't worked with singly-linked lists for a while, so this problem was pretty fun
#
###


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #---------------SECOND ATTEMPT---------------
        l1.val += l2.val

        if l1.val > 9: 
            l1.val -= 10
            if l1.next == None:
                l1.next = ListNode(0)
            l1.next.val += 1

        if l1.next != None or l2.next != None:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            l1.next = self.addTwoNumbers(l1.next, l2.next)
        
        return l1
    
        
        
        
        """
        #---------------FIRST ATTEMPT---------------
        
        # obtain forwards order string of values contained in l1
        v = ListNode(l1).val
        l1 = ''
        while v != None:
            l1 = str(v.val) + l1
            v = v.next

        # obtain forwards order string of values contained in l2
        v = ListNode(l2).val
        l2 = ''
        while v != None:
            l2 = str(v.val) + l2
            v = v.next
            
        # add numbers while maintaining string type
        v = str(int(l1) + int(l2))    
        
        # convert sum to reverse order singly linked list
        l1 = ListNode(v[0])
        for i in range(1, len(v)):
            l2 = ListNode(v[i])
            l2.next = l1
            l1 = l2
        return l1
        """
