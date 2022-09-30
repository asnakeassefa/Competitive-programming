# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        temp = head
        while temp:
            x = x + 1
            temp = temp.next
            
        for y in range(int(x/2)):
            head = head.next
            
        return head
        