class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        r = 0
        comm = -1
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                comm = nums1[l]
                break
        
        return comm
        
