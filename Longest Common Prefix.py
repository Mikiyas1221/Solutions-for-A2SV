class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mystr = ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            mystr += strs[0][i]
        return mystr
