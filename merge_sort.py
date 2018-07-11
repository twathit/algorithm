def merge_sort(arr):
	import math
	if len(arr)<2:
		return arr
	middle=math.floor(len(arr)/2)
	left,right=arr[:middle],arr[middle:]
	return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
	result=[]
	while left and right:
		if left[0]<=right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result

if __name__=='__main__':
	print(merge_sort([3,7,24,56,5,9,10,2,7]))