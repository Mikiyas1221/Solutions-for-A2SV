class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return "0"
            prev_str = helper(n - 1)

            arr = [i for i in prev_str]

            for i in range(len(arr)):
                if arr[i] == "0":
                    arr[i] = "1"
                else:
                    arr[i] = "0"
            arr.reverse()
            reversed_str = "".join(arr)
            my_str = prev_str + "1" + reversed_str
            return my_str
        print(helper(n))
        return helper(n)[k-1]
            
