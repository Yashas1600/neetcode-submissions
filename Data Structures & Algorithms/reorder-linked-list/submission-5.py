# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        need to split into two lists
        first list should be longer if it is an odd length 
        I beleive i can do the split with fast and slow pointer
        then i need to reverse link list and basically combine the two lists
        """

        dummy = ListNode(0,head)
        slow,fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        #now second point to the start of the second half/second list
        #now i need to reverse the second list
        prev = None
        cur = second
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        l1 = head
        l2 = prev
        while l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l1 = temp1
            l2.next = l1
            l2 = temp2







