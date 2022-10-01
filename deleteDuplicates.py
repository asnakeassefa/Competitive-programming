# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sta = ListNode(0,head)
        start = sta;
        current = head
        
        while current and current.next:
            if current and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                start.next = current
            else:
                start = current
                current = current.next
        
        return sta.next;