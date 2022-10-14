class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = []
        num1,num2,num3 = nums.count(0),nums.count(1),nums.count(2)
        
        for x in range(num1):
            nums[x] = 0
        for x in range(num2):
            nums[x+num1] = 1
        for x in range(num3):
            nums[x+num1+num2] = 2
            