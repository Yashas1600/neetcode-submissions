# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
           f         
        [1,2,3,4, 5, 6 ,7]
        [1,2,3,4, 5,7]
        remove 2nd last (6th)
        length = 7
        so want to end up at 5th
       
       i think i need a 2 ptr approach
        """
        if not head:
            return None
        dummy = ListNode(0,head)
        fast,slow = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
