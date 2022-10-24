class Solution:
    def longestMountain(self, arr: List[int]) -> int:    
        
        rise = fall = False
        i,mountain = 0,0
        
        while i < len(arr):
            l = i
            while i < len(arr)-1 and arr[i] < arr[i+1]:
                i += 1
                rise = True
            
            if rise:
                while i < len(arr)-1 and arr[i] > arr[i+1]:
                    i += 1
                    fall = True
                    
            if rise and fall:
                mountain = max(mountain, i - l + 1)
                
            else:
                i += 1
            rise = fall = False
            
        return mountain