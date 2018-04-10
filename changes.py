#钱币找零：假设用于找零的钱币包括四种：25美分，10美分，5美分，1美分，求给用户找回数目最少的钱币。

#方法一
def recMC(coinValueList,changes):
	minCoins=changes
	if changes in coinValueList:
		return 1
	else:
		for i in [c for c in coinValueList if c <= changes]:
			numcoins = 1+ recMC(coinValueList,changes-i)
			if numcoins < minCoins:
				minCoins = numcoins
		return minCoins

if __name__ =='__main__':
	print(recMC([1,5,10,25],63))

#方法二：加备忘录装饰器
def memo(f):
	memo={}
	def wrapper(L,x):
		if x not in memo:
			memo[x]=f(L,x)
		return memo[x]
	return wrapper

@memo
def recMC(coinValueList,changes):
	minCoins=changes
	if changes in coinValueList:
		return 1
	else:
		for i in [c for c in coinValueList if c <= changes]:
			numcoins = 1+ recMC(coinValueList,changes-i)
			if numcoins < minCoins:
				minCoins = numcoins
		return minCoins

if __name__ =='__main__':
	print(recMC([1,5,10,25],63))


#方法三：自底向上
def dpMakeChange(coinValueList,changes):
	minCoins={}
	for cents in range(changes+1):
		coinCount=cents
		for i in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-i]+1<coinCount:
				coinCount=minCoins[cents-i]+1
		minCoins[cents]=coinCount
	return minCoins[changes]

if __name__ =='__main__':
	print(dpMakeChange([1,5,10,25],63))


#扩展：同时输出需要哪些钱币
def dpMakeChange(coinValueList,changes):
	minCoins={}
	coinUsed={}
	newcoin=coinValueList[0]
	for cents in range(changes+1):
		coinCount=cents
		for i in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-i]+1<coinCount:
				coinCount=minCoins[cents-i]+1
				newcoin=i
		minCoins[cents]=coinCount
		coinUsed[cents]=newcoin
	return minCoins[changes],coinUsed

def printCoins(coinUsed,changes):
	coin=changes
	thisCoin=[]
	while coin>0:
		thisCoin.append(coinUsed[coin])
		coin=coin-thisCoin[-1]
	print(thisCoin)
if __name__=='__main__':
	coinCount,coinUsed=dpMakeChange([1,5,10,25],63)
	print('The minimum coins are:',coinCount)
	print('They are:')
	printCoins(coinUsed,63)