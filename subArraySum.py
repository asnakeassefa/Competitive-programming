class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Sum,count = 0, 0
        
        pre = {0:1}
        
        for x in nums:

            Sum += x
            if pre.get(Sum - k):
                count += pre.get(Sum - k)
            pre[Sum] = pre.get(Sum,0) + 1
        
        return count