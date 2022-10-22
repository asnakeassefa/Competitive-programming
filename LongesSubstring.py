class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,0
        dic = {}
        
        ans = 0
        
        while r < len(s):
            
            if not dic.get(s[r]):
                
                dic[s[r]] = True
                r += 1
            else:
                
                ans = max(ans,r-l)
                
                dic[s[l]] = False
                l += 1
        
        return max(ans,r - l)
                