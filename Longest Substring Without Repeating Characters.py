class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ""
        i = 0
        size = 0
        for j in range(len(s)):
            if s[j] in s[i:j]:
                while s[i] != s[j]:
                    i += 1
                i += 1
            size = max(size, j - i + 1)
        return size
        
