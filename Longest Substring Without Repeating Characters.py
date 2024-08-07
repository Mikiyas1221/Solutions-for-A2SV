class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ""
        i = 0
        size = 0
        for j in range(len(s)):
            if s[j] not in seen:
                seen = s[i:j+1]
            
            else:
                while s[i] != s[j]:
                    i += 1
                i += 1
                seen = s[i:j+1]
            size = max(size, len(seen))
        return size
        
