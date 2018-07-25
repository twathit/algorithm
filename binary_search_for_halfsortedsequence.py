def binary_search_for_halfsortedsequence(list,item):
	low = 0
	high = len(list)-1
	while low <= high:
		mid = (low+high)//2
		if list[mid]==item:
			return mid
		elif (list[low]<=list[mid] and (item>list[mid] or item<=list[high])) or (list[low]>=list[mid] and (item>list[mid] and item<=list[high])):
			low = mid + 1
		else:
			high = mid - 1
	return None

if __name__ == '__main__':
	print(binary_search_for_halfsortedsequence([4,5,7,8,1,2,3],5))
	print(binary_search_for_halfsortedsequence([1,2,3,4,5,6,7],5))