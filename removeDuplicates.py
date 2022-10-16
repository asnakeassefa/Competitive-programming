# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        Dummy = ListNode()
        tail = Dummy
        if curr:
            node = ListNode(curr.val)
            tail.next = node
            tail = tail.next
            curr = curr.next
        while curr:
            if curr.val == tail.val:
                curr = curr.next
            else:
                node = ListNode(curr.val)
                tail.next = node
                curr = curr.next
                tail = tail.next
        
        return Dummy.next