var getSingleton=(function(){
	function China(){
		this.name='China';
	}
	var instance=new China();
	return function(){
		return instance;
	};
}());

var instance1=getSingleton();
var instance2=getSingleton();

console.log('instance1===instance2 is: '+(instance1===instance2));