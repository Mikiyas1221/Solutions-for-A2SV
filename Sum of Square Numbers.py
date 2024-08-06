class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        k = int(math.sqrt(c))
        ans = False
        for x in range(k+1):
            n = math.sqrt(c - x ** 2)
            if n == int(n) and n < k+1:
                ans = True
                break
        return ans
