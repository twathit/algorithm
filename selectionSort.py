def selection_sort(arr):
	for i in range(len(arr)-1):
		minIndex=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[minIndex]:
				minIndex=j
		if i!=minIndex:
			arr[i],arr[minIndex]=arr[minIndex],arr[i]
	return arr

if __name__=='__main__':
	print(selection_sort([3,7,24,56,5,9,10,2,7]))