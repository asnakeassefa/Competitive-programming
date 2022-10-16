# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        num1 = ''
        num2 = ''
        
        dummy = ListNode()
        tail = dummy
        while l1 or l2:
            if l1:
                num1 += str(l1.val)
                l1 = l1.next
            if l2:
                num2 += str(l2.val)
                l2 = l2.next
        num2 = num2[::-1]
        num1 = num1[::-1]
        # result = str(sum(int(num1),int(num2)))
        SUM = int(num1) + int(num2)
        result = str(SUM)
        result = result[::-1]
        for x in result:
            node = ListNode(x)
            tail.next = node
            tail = tail.next
        
        return dummy.next