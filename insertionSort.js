function insertionSort(arr){
	var len=arr.length;
	var preIndex,current;
	for (var i=1;i<len;i++){
		preIndex=i-1;
		current=arr[i]
		while(preIndex>=0 && arr[preIndex]>current){
			arr[preIndex+1]=arr[preIndex];
			preIndex-=1
		}
		arr[preIndex+1]=current;
	}
	return arr;
}

console.log(insertionSort([3,7,24,56,5,9,10,2,7]));