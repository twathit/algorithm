class Solution:
	def print_matrix(self, matrix, rows, cols):
			for i in range(rows):
				for j in range(cols):
					print(matrix[cols*i+j], end=' ')
				print()
			print('----')

	def has_path(self,matrix,rows,cols,str):
		if len(matrix) ==0 or len(str) == 0 or len(matrix) != cols*rows:
			return False
		for i in range(rows):
			for j in range(cols):
				if self.find_path(list(matrix),rows,cols,str,i,j):
					return True
		return False

	def find_path(self,matrix,rows,cols,str,x,y):
		if not str:
			return True
		haspath=False
		if x<rows and x>=0 and y<cols and y>=0 and matrix[x*cols+y] == str[0]:
			matrix[x*cols+y]='*'
			self.print_matrix(matrix,rows,cols)
			haspath=self.find_path(matrix,rows,cols,str[1:],x-1,y) or self.find_path(matrix,rows,cols,str[1:],x,y-1) or self.find_path(matrix,rows,cols,str[1:],x+1,y) or self.find_path(matrix,rows,cols,str[1:],x,y+1)
			if not haspath:
				matrix[x*cols+y]=str[0]	
		return haspath

if __name__=='__main__':
	s=Solution()
	_matrix='abtgcfcsjdeh'
	_path='bfce'
	_path2='abfb'
	_path3='bfcedjc'
	print(s.has_path(_matrix,3,4,_path))
	print(s.has_path(_matrix,3,4,_path2))
	print(s.has_path(_matrix,3,4,_path3))

