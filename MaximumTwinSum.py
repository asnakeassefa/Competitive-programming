# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = -1
        val = []
        temp = head
        while temp:
            val.append(temp.val)
            temp = temp.next
        
        half = int(len(val)/2) - 1
        print(half)
        
        for x in range(half+1):
            SUM = val[half - x] + val[half+x+1]
            res = max(res,SUM)
        return res