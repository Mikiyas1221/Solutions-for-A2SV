class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 /x
            n = -n
        

        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half ** 2
        else:
            return x * self.myPow(x, n - 1)
