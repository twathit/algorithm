def factors_set():
	factors_set=((i,j,k,l) for i in [-1,0,1]
							for j in [-1,0,1]
							for k in [-1,0,1]
							for l in [-1,0,1])
	return factors_set

def memo(f):
	memo={}
	def wrapper(n):
		if n not in memo:
			memo[n]=f(n)
		return memo[n]
	return wrapper

@memo
def weight(pounds):
	weighs=[1,3,9,27]
	for factors in factors_set():
		sum=0
		for i in range(len(factors)):
			sum+=factors[i]*weighs[i]
		if sum == pounds:
			return factors

if __name__=='__main__':
	for i in range(1,11):
		print(weight(i))