class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ans = []
        point = []
        
        for x in points:
            point.append([(x[0]**2 + x[1] **2),x])
        
        point.sort(key=lambda x:x[0])
        
        for x,y in point:
            ans.append(y)
        
        return ans[:k]
