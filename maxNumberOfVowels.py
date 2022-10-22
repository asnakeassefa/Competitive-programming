class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = {}
        
        for x in "aeiou":
            vowel[x] = 1
        ans = 0
        for x in range(k):
            ans += vowel.get(s[x],0)
        l,r = 0,k
        temp = ans
        for x in range(k,len(s)):
            
            temp += vowel.get(s[r],0)
            temp -= vowel.get(s[l],0)
    
            ans = max(ans,temp)
            l += 1
            r += 1
        
        return ans