class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        kth_0 = -1
        for i in range(len(nums)):
            if l == k:
                break
            if nums[i] == 0:
                l += 1
                kth_0 = i
        i = 0
        size = kth_0 + 1
        for j in range(kth_0 + 1, len(nums)):
            if nums[j] == 0:
                while nums[i] != 0:
                    i += 1
                i += 1
                size = max(size, j - i + 1)
            size = max(size, j - i + 1)
        return size
