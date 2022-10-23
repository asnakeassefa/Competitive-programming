class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        """
        0,1,1,1,0,1,1,0,1
                
        """
        
        temp = 0
        l,r = 0,0
        
        ans = 0
        for x in nums:
            if x == 0:
                temp += 1
                ans = max(ans,l+r)
                l = r
                r = 0
            else:
                r += 1
        ans = max(ans,l+r)
        
        if temp == 0:
            ans = len(nums) - 1
        
        return ans