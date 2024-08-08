class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = "/"
        arr = []
        temp = ""
        for i in range(1, len(path)):
            if path[i] == "/":
                if temp != "":
                    arr.append(temp)
                temp = ""
            else:
                temp += path[i]
                if i == len(path) - 1:
                    arr.append(temp)
        i = 0
        while i < len(arr):
            if arr[i] == "..":
                if i > 0:
                    arr.pop(i-1)
                    i -= 1
                arr.pop(i)
                i -= 1
            elif arr[i] == ".":
                arr.pop(i)
                i -= 1
            i += 1
        ans += "/".join(arr)
        return ans
