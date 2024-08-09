class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for c in tokens:
            if c == "+":
                temp = result[-2] + result[-1]
                result.pop(-1)
                result.pop(-1)
                result.append(temp)
            elif c == "-":
                temp = result[-2] - result[-1]
                result.pop(-1)
                result.pop(-1)
                result.append(temp)
            elif c == "*":
                temp = result[-2] * result[-1]
                result.pop(-1)
                result.pop(-1)
                result.append(temp)
            elif c == "/":
                temp = result[-2] / result[-1]
                result.pop(-1)
                result.pop(-1)
                result.append(int(temp))
            else:
                result.append(int(c))
        return result[0]
