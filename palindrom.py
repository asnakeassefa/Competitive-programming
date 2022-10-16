# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        val = []
        res=True
        while curr:
            val.append(curr.val)
            curr = curr.next
        print(val)
        for x in range(len(val)):
            if head.val != val[-(x+1)]:
                res = False
            head = head.next
        
        return res