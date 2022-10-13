# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pre,slow,fast = None,head,head
        
        for x in range(n):
            fast = fast.next
        if fast == None and n == 1:
            return None
        while fast:
            pre = slow
            fast = fast.next
            slow = slow.next
            
        if slow:
            if slow == head:
                pre = head
                head = head.next
                del pre
            else:
                pre.next = slow.next
                del slow
        return head