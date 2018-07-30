class Solution:
	def max_product_after_cutting1(self,n):
		if n<2:
			return 0
		if n==2:
			return 1
		if n==3:
			return 2
		max_list=[0,1,2,3]
		for i in range(4,n+1):
			max=0
			for j in range(1,i//2+1):
				temp=max_list[j]*max_list[i-j]
				if temp>max:
					max=temp
			max_list.append(max)
		return max_list[n]

	def max_product_after_cutting2(self,n):
		if n<2:
			return 0
		if n==2:
			return 1
		if n==3:
			return 2
		max_list=[0,1,2,3]
		timesof3=n//3
		if n-timesof3*3==1:
			timesof3=timesof3-1
		timesof2=(n-timesof3*3)//2
		return (3**timesof3)*(2**timesof2)

print(Solution().max_product_after_cutting1(8))
print(Solution().max_product_after_cutting2(8))
