def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

if __name__=='__main__':
	print(bubble_sort([3,7,24,56,5,9,10,2,7]))