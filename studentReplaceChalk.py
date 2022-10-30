class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        x = 0
        
        y = sum(chalk)
        k = k % y
        
        while chalk[x] <= k:
            
            k = k - chalk[x]
            x += 1
            if x == len(chalk):
                x = 0
                
        return x