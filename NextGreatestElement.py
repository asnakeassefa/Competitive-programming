class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        """
        
        
        """
        temp = -1
        ans = []
        for x in nums1:
            i = nums2.index(x)
            i += 1
            while i < len(nums2):
                if x < nums2[i]:
                    temp = nums2[i]
                    break
                else:
                    i += 1
            ans.append(temp)
            temp = -1
        return ans
                