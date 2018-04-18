'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

def find_target(matrix,target):
	found=False
	if not matrix or target is None:
		return found
	rows = len(matrix)
	columns = len(matrix[0]) 
	if matrix and rows > 0 and columns>0:
		row=0
		column=columns-1
		while row<rows and column>=0: 
			if matrix[row][column] == target:
				found=True
				break
			elif matrix[row][column]>target:
				column-=1
			else:
				row+=1
	return found

if __name__=='__main__':
	print(find_target([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],7))