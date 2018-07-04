var len;
function buildHeap(arr){		//建立大顶堆
	len=arr.length;
	for (var i = Math.floor(len/2)-1;i>=0;i--){
		heapify(arr,i);
	}
}

function heapify(arr,i){
	var left=2*i+1,
		right=2*i+2,
		largest=i;
	if(left<len && arr[left]>arr[largest] &&arr[left]>arr[right]){
		largest=left
	}
	if(right<len && arr[right]>arr[largest] && arr[right]>arr[left]){
		largest=right
	}

	if(largest!==i){
		swap(arr,i,largest);
		heapify(arr,largest);
	}
}

function swap(arr,i,j){
	var temp=arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
}

function heapSort(arr){
	buildHeap(arr);
	for(var i=len-1;i>0;i--){
		swap(arr,0,i);
		len--;
		heapify(arr,0);
	}
	return arr;
}

console.log(heapSort([3,7,24,56,5,9,10,2,7]))