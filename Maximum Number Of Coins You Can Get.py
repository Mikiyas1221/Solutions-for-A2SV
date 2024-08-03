class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = len(piles) - 2
        l = 0
        ans = 0
        while l < i:
            ans += piles[i]
            l += 1
            i -= 2
        return ans
