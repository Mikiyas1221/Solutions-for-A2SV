class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for i in range(n - 2)] for j in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                my_max = 0
                for k in  range(i, i+3):
                    for p in range(j, j+3):
                        my_max = max(my_max, grid[k][p])
                ans[i][j] = my_max
        return ans
