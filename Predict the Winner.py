class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return nums[left]
            
            left_score = nums[left] - helper(left + 1, right)
            right_score = nums[right] - helper(left, right - 1)

            return max(left_score, right_score)
        
        return helper(0, len(nums) - 1) >= 0
