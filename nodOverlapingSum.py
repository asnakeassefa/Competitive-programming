class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
    
        prefixSum = [0] * (len(nums) + 1)
        
        for x in range(len(nums)):
            prefixSum[x + 1] = prefixSum[x] + nums[x]
        
        def findSum(prefix,f,s):
            max1,max2 = 0, 0
            for y in range(len(prefix) - f - s):
                first = prefix[y + f] - prefix[y]
                second = prefix[y+f+s] - prefix[y + f]
                
                max1 = max(max1, first)
                max2 = max(max2,max1+second)
            return max2
        
        maxsum1 = findSum(prefixSum,firstLen,secondLen)
        maxsum2 = findSum(prefixSum,secondLen,firstLen)
        
        return max(maxsum1,maxsum2);