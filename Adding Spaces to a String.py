class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        mod_s = ""
        k = 0
        for i in range(len(s)):
            if k < len(spaces) and i == spaces[k]:
                mod_s += " "
                k += 1
            mod_s += s[i]
        return mod_s
        
