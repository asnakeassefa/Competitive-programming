class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = None
        leftsum = [0] * len(nums)
        exist = False
        presum = [0] * (len(nums))
        presum[0] = nums[0]
        for x in range(1,len(nums)):
            presum[x] = presum[x-1] + nums[x]
        
        print(presum[0])
        
        for x in range(0,len(presum)):
            leftsum[x] = presum[x]
            if leftsum[x-1] == (presum[-1] - presum[x]):
                index = x
                exist = True
                break
        if not exist:
            index = -1
        return index