class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                char = int(s[i] + s[i+1])
                ans += chr(96 + char)
                i += 1
            elif s[i] != '#':
                char = int(s[i])
                ans += chr(96 + char)
            i += 1
        return ans
