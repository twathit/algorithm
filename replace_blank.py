'''请实现一个函数，将一个字符串中的空格替换成“%20”。 
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。'''

def replace_blank(string):
	length=len(string)
	blankNumber=0
	if length == 0:
		return None
	for i in range(length):
		if string[i]==' ':
			blankNumber+=1
	if not  blankNumber:
		return string
	newLength = length + blankNumber*2
	newStringList = [' ']*newLength
	indexOfOrigin = length-1
	indexOfNew = newLength-1
	while indexOfOrigin>=0:
		if string[indexOfOrigin]!=' ':
			newStringList[indexOfNew]=string[indexOfOrigin]

			indexOfNew-=1
		else:
			newStringList[indexOfNew]='0'
			indexOfNew-=1
			newStringList[indexOfNew]='2'
			indexOfNew-=1
			newStringList[indexOfNew]='%'
			indexOfNew-=1
		indexOfOrigin-=1
	newString=''
	for i in range(newLength):
		newString+=str(newStringList[i])
	return newString

if __name__=='__main__':
	print(replace_blank('we are happy'))
	print(replace_blank('we  are happy'))
	print(replace_blank(''))
	print(replace_blank('happy'))