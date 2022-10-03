class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current,start,length,top = 0,0,0,[]
        
        for x in range(len(s)):
            for y in range(len(s) - x):
                if top.count(s[x+y]) < 1:
                    top.append(s[x+y])
                    length = max(length,len(top))
                else:
                    length = max(length,len(top))
                    top.clear()
                    break
        return length