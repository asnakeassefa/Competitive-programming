class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count = [0]*len(nums);
        for x in range(len(nums)):
            for y in range(len(nums)):
                if(nums[x] > nums[y]):
                    count[x] += 1
        return count