class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        pre = {0:1}
        ans = 0
        SUM = 0
        for x in range(len(nums)):
            nums[x] = nums[x] % 2
        for y in nums:
            SUM += y
            if pre.get(SUM - k):
                ans += pre.get(SUM - k)
            pre[SUM] = pre.get(SUM,0) + 1
        return ans