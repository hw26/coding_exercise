

class Matrix:

	def __init__(self,matrix):
		self.matrix = matrix
		m = len(matrix)
		n = len(matrix[0])
		self.m = m
		self.n = n

		self.prefix = [[0 for _ in range(n+1)] for _ in range(m + 1)]
		for ii in range(1,m+1):
			for jj in range(1,n+1):
				self.prefix[ii][jj] = self.prefix[ii][jj-1] + self.matrix[ii-1][jj-1]
		for ii in range(1,m+1):
			for jj in range(1,n+1):
				self.prefix[ii][jj] += self.prefix[ii-1][jj]
	def update(self,i,j,val):
		self.matrix[i][j] = val
		for ii in range(i+1,self.m+1):
			for jj in range(j+1,self.n+1):
				self.prefix[ii][jj] += val
	def sum(self,i1,j1,i2,j2):
		print(self.prefix)
		return self.prefix[i2+1][j2+1] - self.prefix[i1][j2+1] - self.prefix[i2+1][j1] + self.prefix[i1][j1]

mat = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(mat.sum(1,1,2,2))
print(mat.sum(1, 0, 1, 1))
print(mat.sum(1, 0, 2, 1))
mat.update(2,2,10)
print(mat.sum(1,1,2,2))


ready = [1,2,3,4]
import heapq
def get_max_priority(unit,ready):
    if not ready:
        return
    head = heapq.heappop(ready)
    reserve = []
    

    while ready and head !=unit:
    	reserve.append(head)
        head =  heapq.heappop(ready)
    for ii in reserve:
    	heapq.heappush(ready,ii)
    return head
    # return head
print get_max_priority(3,ready)