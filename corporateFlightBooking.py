class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        temp = [0] * (n+1)
        res = [0] * (n+1)
        for x in range(len(bookings)):
            temp[bookings[x][1]] += bookings[x][2]
            
            if bookings[x][0]-1 > 0:
                temp[bookings[x][0]-1] += -bookings[x][2]
        
        res[-1] = temp[-1]
        
        for x in range(len(temp)-2,0,-1):
            res[x] = res[x+1] + temp[x]
        
        return res[1:]