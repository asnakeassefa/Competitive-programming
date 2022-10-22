class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        l,r = 0,len(p)
        ans = []
        count1 = {}
        count2 = {}
        
        for x in range(len(p)):
            count2[p[x]] = 1 + count2.get(p[x],0)
            count1[s[x]] = 1 + count1.get(s[x],0)
        
        if count1 == count2:
            ans = [0]
            
        for x in range(r,len(s)):
            
            count1[s[r]] = 1 + count1.get(s[r],0)
            count1[s[l]] -= 1
            
            if count1[s[l]] == 0:
                count1.pop(s[l])
            
            l += 1
            
            if count1 == count2:
                ans.append(l)
            
            r += 1
        
        return ans
                