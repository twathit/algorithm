'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

class Solution:
	def print_matrix(self, matrix, rows, cols):
			for i in range(rows):
				for j in range(cols):
					print(matrix[i][j], end=' ')
				print()
	def check(self,threshold,i,j):
		if sum(map(int,str(i)+str(j)))<=threshold:
			return True
		return False

	def find_grid(self,threshold,matrix,rows,cols,i,j):
		count = 0
		if i<rows and j<cols and i>=0 and j>=0 and self.check(threshold,i,j) and matrix[i][j]==0:
			matrix[i][j]=1
			count=1+self.find_grid(threshold,matrix,rows,cols,i-1,j)+self.find_grid(threshold,matrix,rows,cols,i,j-1)+self.find_grid(threshold,matrix,rows,cols,i+1,j)+self.find_grid(threshold,matrix,rows,cols,i,j+1)
		return count

	def moving_count(self,threshold,rows,cols):
		matrix=[[0 for i in range(cols)] for j in range(rows)]
		count=self.find_grid(threshold,matrix,rows,cols,0,0)
		self.print_matrix(matrix,rows,cols)
		return count

if __name__=='__main__':
	s=Solution()
	print(s.moving_count(10,20,20))
