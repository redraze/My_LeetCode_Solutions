class Solution:
    # Runtime O(n^2)
    # Space complexity O(n^2)
    def findCircleNum(self, mat: List[List[int]]) -> int:
        def connectProvinces(i,row):
            for j,val in enumerate(row):
                if val == 1 and (j,j) not in searched:
                    searched.add((j,j))
                    connectProvinces(j, mat[j])
            return
        searched = set()
        provinces = 0
        # checks the reminder of each row starting from the diagonal of the matrix.
        # if any connections are not in the 'searched' set, then searches recursively 
        # through each of those connections for more connections. Only when an unsearched 
        # node is found along the diagonal has another new province been found.
        for i,row in enumerate(mat):
            if (i,i) not in searched:
                searched.add((i,i))
                provinces += 1
                connectProvinces(i,row)
        return provinces                
