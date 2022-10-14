class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index = []
        for x in range(len(nums) - 1):
            min_index = x
            for y in range(x+1,len(nums)):
                if nums[min_index] > nums[y]:
                    min_index = y
            temp = nums[min_index]
            nums[min_index] = nums[x]
            nums[x] = temp
            
        for x in range(len(nums)):
            if nums[x] == target:
                index.append(x)
        return index
                