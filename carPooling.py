class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        m = max(trips,key=lambda x:x[2])
        k = m[2]
        
        cap = max(trips,key=lambda x:x[0])
        
        if cap[0] > capacity:
            return False
        
        temp = res = [0] * (k + 1)
        
        for x in range(len(trips)):
            
            temp[trips[x][2]] += trips[x][0]
            temp[trips[x][1]] += -trips[x][0]
            
        
        res[-1] = temp[-1]
        
        for x in range(len(temp)-2,0,-1):
            res[x] = res[x+1] + temp[x]
            
            if res[x] > capacity:
                return False
            
        return True
            