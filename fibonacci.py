def fabnacci(n):
	result={0:0,1:1}
	if n <= 0:
		return 0
	if n == 1:
		return 1
	if n not in result:
		result[n] = fabnacci(n-1)+fabnacci(n-2)
	return result[n]


def fabnacci2(n,ret1,ret2):
	if n == 0:
		return ret1
	else:
		return fabnacci2(n-1,ret2,ret1+ret2)

def fabnacci3(max):
	n,a,b = 0,0,1
	while n<max:
		a,b = b,a+b
		n = n+1
	return a

if __name__ == '__main__':
	import time
	start =time.time()
	print(fabnacci(20))
	print(time.time()-start)
	start =time.time()
	print(fabnacci2(100,0,1))
	print(time.time()-start)
	start =time.time()
	print(fabnacci3(100))
	print(time.time()-start)