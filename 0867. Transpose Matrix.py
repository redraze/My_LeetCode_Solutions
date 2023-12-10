class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = [[] for _ in range(len(matrix[0]))]

        for row in matrix:
            for i, num in enumerate(row):
                ret[i].append(num)

        return ret
