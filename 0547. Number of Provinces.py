class Solution:
    def findCircleNum(self, mat: List[List[int]], provinces=0) -> int:
        def connectProvinces(i,row,provinces):
            for j,val in enumerate(row):
                if val == 1 and (j,j) not in searched:
                    searched.add((j,j))
                    provinces += 1
                    connectProvinces(j, mat[j], provinces)
            return
        searched = set()
        for i,row in enumerate(mat):
            if (i,i) not in searched:
                searched.add((i,i))
                provinces += 1
                connectProvinces(i, row, provinces)
        return provinces                
