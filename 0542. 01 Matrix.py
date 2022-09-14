# I chose 'deque' from the 'collections' module to maintain my queue because the runtime of 'popleft()' is O(1).
# This is much faster than the operational runtime of O(n) for 'pop(0)' while using a primitive python list.
from collections import deque
import itertools

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        # memoize squares that have been checked to prevent re-checking
        mem = set()
        # maintain queue of squares that need their surroudning squares checked
        q = deque()
        
        # First pass:
        # memoize and queue quares that contain zeros
        for i,j in itertools.product(range(m), range(n)):
            if mat[i][j] == 0:
                mem.add((i,j))
                q.append((i,j))
            
        # Second pass:
		# use the previously memoized and queued squares that countain zero to 
		# iteratively compute the distances for the remaining non-memoized squares
		while q: # is not empty
			i,j = q.popleft()
			# check up
			if i > 0 and (i-1,j) not in mem: 
				mat[i-1][j] = mat[i][j] + 1
				mem.add((i-1,j))
				q.append((i-1,j))
			# check down
			if i < m-1 and (i+1,j) not in mem:
				mat[i+1][j] = mat[i][j] + 1
				mem.add((i+1,j))
				q.append((i+1,j))
			# check left
			if j > 0 and (i,j-1) not in mem:
				mat[i][j-1] = mat[i][j] + 1
				mem.add((i,j-1))
				q.append((i,j-1))
			# check right
			if j < n-1 and (i,j+1) not in mem:
				mat[i][j+1] = mat[i][j] + 1
				mem.add((i,j+1))
				q.append((i,j+1))
		return mat
