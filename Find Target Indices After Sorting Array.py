class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        myarr = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                myarr.append(i)
        return myarr
        
