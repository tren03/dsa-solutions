# SC = o(1)
# TC = o(mn)
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        
        first_row_zero = False
        first_col_zero = False

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
            
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        for j in range(n):
            if first_row_zero == True:
                matrix[0][j] = 0
        
        for i in range(m):
            if first_col_zero == True:
                matrix[i][0] = 0


        
      


        


        
