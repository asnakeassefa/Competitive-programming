class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        for x in range(len(nums)):
            nums[x] = int(nums[x])
        
        nums.sort(reverse = True)
        
        return str(nums[k-1])
            