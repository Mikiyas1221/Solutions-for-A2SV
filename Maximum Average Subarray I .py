class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        sum_of_window = 0
        for i in range (k):
            sum_of_window += nums[i]
        max_sum = sum_of_window
        while r < len(nums):
            sum_of_window = sum_of_window + nums[r] - nums[l]
            max_sum = max(max_sum, sum_of_window)
            l += 1
            r += 1

        return float(max_sum / k)
