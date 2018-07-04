function selectionSort(arr){
	var len=arr.length;
	var minIndex,temp;
	for(var i=0;i<len-1;i++){
		minIndex=i;
		for(var j=i+1;j<len;j++){
			if (arr[j]<arr[minIndex])
				minIndex=j;
		}
		if (i!=minIndex){
			temp=arr[i];
			arr[i]=arr[minIndex];
			arr[minIndex]=temp;
		}
	}
	return arr;
}

console.log(selectionSort([3,7,24,56,5,9,10,2,7]));