class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        """
        ababcbaca defegde hijhklij
        
        """
        ans = []
        dic = {}
        
        count,end = 0,0
        
        for x in range(len(s)):
            dic[s[x]] = x
            
        for x in range(len(s)):
            count += 1
            end = max(end,dic[s[x]])
            
            if  end == x:
                ans.append(count)
                count = 0
                
        return ans
            