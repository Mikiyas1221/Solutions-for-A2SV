class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        toe = True
        for k in range(len(matrix)-1):
            i = 0
            while i < len(matrix[k])-1:
                if matrix[k][i] == matrix[k+1][i+1]:
                    i += 1
                else:
                    toe = False
                    break
            if not toe:
                break
        return toe
