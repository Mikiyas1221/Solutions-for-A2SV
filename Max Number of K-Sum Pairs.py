class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ans = 0
        seen = []
        for num in c:
            if k - num in c and num not in seen:
                if num == k - num:
                    ans += c[num] // 2
                else:
                    ans += min(c[num], c[k - num])
                seen.append(num)
                seen.append(k - num)
        return ans
