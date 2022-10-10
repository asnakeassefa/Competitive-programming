class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l,r = 0, k
        count = 0
        total = sum(arr[l:r])
        if total >= threshold * k:
            count+=1
        while r < len(arr):
            total += (arr[r] - arr[l])
            if total >= threshold * k:
                count += 1
            l+=1
            r+=1
        return count