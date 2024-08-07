class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        ans = []
        size = 0
        end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])
            if i == end:
                ans.append(size)
                size = 0
        return ans
