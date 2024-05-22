class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose_matrix = []
        for i in range(len(matrix[0])):
            element=[]
            for j in range(len(matrix)):
                element.append(matrix[j][i])
            transpose_matrix.append(element)
        return transpose_matrix
