class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26
        l = 0
        size = 0
        for r in range(len(s)):
            counter[ord(s[r]) - 65] += 1
            #(r-l+1) - max(counter) => no of changeable letters
            while (r - l + 1) - max(counter) > k:
                counter[ord(s[l]) - 65] -= 1
                l += 1
            size = max(size, r - l + 1)
        return size
