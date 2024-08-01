class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        z = len(arr)
        def flipper(k):
            start = 0
            end = k
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            return arr
        ans = []
        temp = [arr[i] for i in range(z)]
        while len(temp) > 0:
            max_no = max(temp)
            ans.append(arr.index(max_no) + 1)
            flipper(arr.index(max_no))
            ans.append(z)
            flipper(z - 1)
            z -= 1
            temp.remove(max_no)
        return ans
