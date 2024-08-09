class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        value = 0
        ans = 0
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                m = stack.pop()
                if m == 0:
                    val = 1
                else:
                    val = m * 2
                if stack:
                    stack[-1] += val
                else:
                    ans += val
        return ans
        
