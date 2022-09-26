class Solution:
    # Runtime O(n^2)
    # Space complexity O(n^2)
    def findCircleNum(self, mat: List[List[int]]) -> int:
        # check row for connections
        def connectProvinces(i,row):
            for j,val in enumerate(row):
                if val == 1 and (j,j) not in searched:
                    searched.add((j,j))
                    connectProvinces(j, mat[j])
            return
        searched = set()
        provinces = 0
        # iterate down the diagonal for unsearched provinces
        for i,row in enumerate(mat):
            if (i,i) not in searched:
                searched.add((i,i))
                provinces += 1
                connectProvinces(i,row)
        return provinces                
