function quickSort(L,low,high){
	var i=low,j=high;
	if (i>=j){
		return L
	}
	var key=L[i];
	while (i!==j){
		while(i<j && L[j]>=key){
			j=j-1
		}
		L[i]=L[j]
		while(i<j && L[i]<=key){
			i=i+1
		}
		L[j]=L[i]
	}
	L[i]=key
	quickSort(L,low,i-1)
	quickSort(L,i+1,high)
	return L
}

console.log(quickSort([3,7,24,56,5,9,10,2,7],0,8))