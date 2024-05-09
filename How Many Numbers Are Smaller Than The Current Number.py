class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        myarr = []
        for i in nums:
            counter = 0
            for j in range(len(nums)):
                if nums[j] < i:
                    counter += 1
            myarr.append(counter)
        return myarr
