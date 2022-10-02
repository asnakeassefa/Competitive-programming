class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroflip, start, maximum = 0, 0, 0
        
        for x in range(len(nums)):
            if nums[x] ==  0:
                zeroflip += 1
            while zeroflip > k:
                if nums[start] == 0:
                    zeroflip -= 1
                start += 1
            maximum = max(maximum, x-start + 1)
        return maximum