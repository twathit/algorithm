function bubbleSort(arr){
	var len=arr.length;
	for (var i=0;i<len;i++){
		for (var j=0;j<len-i-1;j++){
			if (arr[j]>arr[j+1]){
				var temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
			
		}
	}
	return arr;
}

console.log(bubbleSort([3,7,24,56,5,9,10,2,7]))