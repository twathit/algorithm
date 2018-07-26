def find_minimum_in_rotated_sorted_array(list):
	if len(list)==0:
		return None
	low = 0
	high = len(list)-1
	mid = low
	while (list[low]>=list[high]):
		if high - low ==1:
			mid = high
			break
		mid = (low+high)//2
		if (list[low]==list[high] and list[low]==list[mid]):
			return min_in_order(list,low,high)
		if list[low]<=list[mid]:
			low = mid
		elif list[high]>=list[mid]:
			high = mid
	return list[mid]

def min_in_order(list,low,high):
	result = list[low]
	for i in range(1,high+1):
		if result>list[i]:
			result=list[i]
	return result

def find_min(list):
	low = 0
	high = len(list)-1
	mid = low
	while low<high:
		mid = (low+high)//2
		if list[mid]>list[high]:
			low = mid+1
		elif list[mid]<list[high]:
			high =mid
		else:
			high = high-1
	return list[low]


if __name__ == '__main__':
	print(binary_search_for_minimum([4,5,7,8,1,2,3]))
	print(binary_search_for_minimum([1,2,3,4,5,6,7]))
	print(binary_search_for_minimum([1,0,1,1,1]))