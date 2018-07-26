'''
81. Search in Rotated Sorted Array II
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''

def search_in_rotated_sorted_array(list,item):
	if len(list)==0:
		return -1
	low = 0
	high = len(list)-1
	while low <= high:
		mid = (low+high)//2
		if list[mid]==item:
			return mid
		if (list[low]==list[mid] and list[high]==list[mid]):
            low=low+1
            high=high-1
		elif (list[low]<=list[mid] and (item>list[mid] or item<list[low])) or (list[low]>=list[mid] and (item>list[mid] and item<list[low])):
			low = mid + 1
		else:
			high = mid - 1
	return -1

if __name__ == '__main__':
	print(binary_search_for_halfsortedsequence([4,5,7,8,1,2,3],5))
	print(binary_search_for_halfsortedsequence([1,2,3,4,5,6,7],5))