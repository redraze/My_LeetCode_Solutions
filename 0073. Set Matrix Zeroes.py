class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # O(1) space solution

        # check first row for a zero
        row0 = 1
        for num in matrix[0]:
            if num == 0:
                row0 = 0
        
        # check first column for a zero
        col0 = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = 0

        # check rest of matrix for zeroes. if a zero is found,
        # mark the edges with zeros for later
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # zero out rows and columns marked with an initial zero
        # (skip row 0 and column 0 for now)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # check row 0 and column 0
        if row0 == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return matrix


        # # O(m + n) space solution
        # rows, columns = set(), set()
        
        # # mark each row and column to be zeroed
        # for i, row in enumerate(matrix):
        #     for j, num in enumerate(row):
        #         if num == 0:
        #             matrix[i]
        #             rows.add(i)
        #             columns.add(j)

        # # zero out the marked rows
        # for row in rows:
        #     for i in range(len(matrix[0])):
        #         matrix[row][i] = 0

        # # zero out the marked columns
        # for column in columns:
        #     for i in range(len(matrix)):
        #         matrix[i][column] = 0

        # return matrix
