class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        counter_p = {}
        counter_s = {}
        temp = {}
        for c in p:
            if c not in counter_p:
                counter_p[c] = 1
            else:
                counter_p[c] += 1
        for c in p:
            counter_s[c] = 0
            temp[c] = 0
        l = 0
        for r in range(len(s)):
            if s[r] in p:
                counter_s[s[r]] += 1
            if r - l + 1 == len(p):
                if counter_s == counter_p:
                    ans.append(l)
                if s[l] in p:
                    counter_s[s[l]] -= 1
                l += 1
        return ans
