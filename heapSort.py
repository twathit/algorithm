
def buildSort(arr):
	import math
	for i in range(math.floor(len(arr)/2)-1,-1,-1):
		heapify(arr,i)

def heapify(arr,i):
	left=2*i+1
	right=2*i+2
	largest=i
	if left<length and arr[left]>arr[largest]:
		largest=left
	if right<length and arr[right]>arr[largest]:
		largest=right
	if largest!=i:
		swap(arr,i,largest)
		heapify(arr,largest)

def swap(arr,i,j):
	arr[i],arr[j]=arr[j],arr[i]

def heapSort(arr):
	global length
	length=len(arr)
	buildSort(arr)
	for i in range(len(arr)-1,0,-1):
		swap(arr,0,i)
		length-=1
		heapify(arr,0)
	return arr

if __name__=='__main__':
	print(heapSort([3,7,24,56,5,9,10,2,7]))