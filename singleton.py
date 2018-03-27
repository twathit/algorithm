#单例模式

#方法一：单线程
class Singleton(object):
	_instance = None

	def __new__(cls, *arg,**kw):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(cls, *arg, **kw)      # __new__用来创建实例,__init__用来初始化实例
		return cls._instance

if __name__ == '__main__':
	s = Singleton()
	print('object created :', id(s))
	t = Singleton()
	print('object created :', id(t))

#方法二：多线程
import threading

class Singleton(object):		#只有第一次创建实例时需要加锁，其它时候无需加锁，只需判断，提高效率
	_instance = None

	def __new__(cls, *arg, **kw):       #__new__里面的cls表示当前类Singleton
		if not cls._instance:
			cls._instance_lock = threading.Lock()		#创建锁前判断一次
			
			if not cls._instance:
				with cls._instance_lock:		#获得锁前判断一次
					cls._instance = super(Singleton, cls).__new__(cls, *arg, **kw)
		return cls._instance

if __name__ == '__main__':
	def task():
		obj = Singleton()
		print('Object created :', id(obj))

	for i in range(5):
		t = threading.Thread(target=task)
		t.start()
		t.join()


#方法三：运用元类
import threading

class MetaSingleton(type):
	_instance = {}
	_instance_lock = threading.Lock()

	def __call__(cls, *args, **kwargs):         #__call__里面的cls表示超类的类Singleton
		if cls not in MetaSingleton._instance:
			with MetaSingleton._instance_lock:
				MetaSingleton._instance[cls] = super().__call__(cls, *args, **kwargs)
		return MetaSingleton._instance[cls]

class Singleton(metaclass=MetaSingleton):
	pass

if __name__ == '__main__':
	def task():
		obj = Singleton()
		print('Object created :',id(obj))

	for i in range(5):
		t = threading.Thread(target=task)
		t.start()
		t.join()