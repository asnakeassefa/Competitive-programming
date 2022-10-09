#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for x in range(len(arr) - 1):
            min_index = x
            for y in range(x+1,len(arr)):
                val = select(arr,min_index)
                val2 = select(arr,y)
                if val > val2:
                    min_index = y
            
            temp = arr[min_index]
            arr[min_index] = arr[x]
            arr[x] = temp
        return arr
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends