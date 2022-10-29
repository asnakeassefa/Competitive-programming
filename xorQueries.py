class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        res = []
        pre = [0] * len(arr)
        pre[0] = arr[0]
        
        for x in range(1,len(arr)):
            pre[x] = pre[x-1] ^ arr[x]
        
        for x in range(len(queries)):
            if queries[x][0] > 0:
                res.append(pre[queries[x][1]] ^ pre[queries[x][0]-1])
            elif queries[x][0] == 0:
                res.append(pre[queries[x][1]])
        return res