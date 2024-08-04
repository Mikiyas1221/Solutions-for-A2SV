class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            j = len(nums1) - 1
            nums1.pop(j)
        nums1 += nums2
        nums1.sort()
