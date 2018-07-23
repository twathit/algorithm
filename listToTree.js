function listToTree(list,parentId){
	var temp=[];
	var noChild=false;
	for (var i in list){
		if (list[i].parent===parentId){
			for (var j in list){
				if (list[j].parent===list[i].id){
					list[i].child=listToTree(list,list[i].id);
				}

			}
			temp.push(list[i]);	
									
		}		
	}
	return temp[0];
}

var list=[
	{ id: 1, name: 'AAAA', parent: 0},
    { id: 2, name: 'AAAA1', parent: 1},
    { id: 3, name: 'AAAA2', parent: 2}
];
console.log(listToTree(list,0));