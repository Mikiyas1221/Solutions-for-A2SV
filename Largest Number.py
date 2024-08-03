class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        str_nums.sort(reverse = True)
        for i in range(len(nums) - 1):
            if str_nums[i] + str_nums[i+1] < str_nums[i+1] + str_nums[i]:
                str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                j = i
                while str_nums[j - 1] + str_nums[j] < str_nums[j] + str_nums[j - 1] and j > 0:
                    str_nums[j], str_nums[j - 1] = str_nums[j - 1], str_nums[j]
                    j -= 1
        if str_nums[0] == "0":
            return "0"
        return "".join(str_nums)

