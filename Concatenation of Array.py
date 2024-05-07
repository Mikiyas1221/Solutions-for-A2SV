class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list = []
        i = 0
        while i < len(nums):
            list.append(int(nums[i]))
            i += 1
        list = list +list
        return list
        
