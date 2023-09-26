class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def dp(L: int, R: int, matrix: List[List[int]]) -> None:
            if L >= R:
                return
            for i in range(R - L):
                temp = matrix[L][L + i]
                matrix[L][L + i] = matrix[R - i][L]
                matrix[R - i][L] = matrix[R][R - i]
                matrix[R][R - i] = matrix[L + i][R]
                matrix[L + i][R] = temp
            L, R = L + 1, R - 1
            dp(L ,R, matrix)
            return

        L, R = 0, len(matrix) - 1
        dp(L, R, matrix)
        return
