def insertion_sort(arr):
	for i in range(1,len(arr)):
		preIndex=i-1
		current=arr[i]
		while  preIndex>=0 and arr[preIndex]>current:
			arr[preIndex+1]=arr[preIndex]
			preIndex-=1
		arr[preIndex+1]=current
	return arr

if __name__=='__main__':
	print(insertion_sort([3,7,24,56,5,9,10,2,7]))