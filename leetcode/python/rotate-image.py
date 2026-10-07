TC = o(n^2), as we do a reverse for every row
SC = o(1) only, ony inplace modifications
inuition - solved this using observation, think transpose + reverse
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i,n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        for i in range(n):
            matrix[i].reverse()

        
