class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] not in stack:
                while len(stack) > 0 and stack[-1] in s[i:] and s[i] < stack[-1]:
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)
