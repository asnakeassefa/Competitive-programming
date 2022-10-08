class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,post = 1,1
        l = len(nums)
        
        output = [1] * len(nums)
        output[0] = output[pre]
        for x in range(len(nums)):
            output[x] = pre
            pre = pre * nums[x]
        for y in range(l):
            output[l-1 - y] *= post
            post *= nums[l-1 - y]
        return output
            