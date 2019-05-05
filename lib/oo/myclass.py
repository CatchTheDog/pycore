'''
python面向对象练习
self 指向当前类实例，非关键词，换成其他名称也可
self.class指向类
'''

class MyClass:
	'''一个简单的类实例'''
	def __init__(self,name):
		print('init.')
		self.name = name #构造函数中定义实例属性
		self.job = 'xyz'
	#类基本属性
	i = 12345
	name = 'hhhhi' #这里赋值和在构造函数中赋值有不同吗？————这里定义的变量，使用对象访问则是实例属性，使用类方法则是类的静态属性
	__age = 10 #私有属性
	
	def f(self):
		return 'Hello world.'
	
	def __privatefunc(self):
		return 'I am a private function.'
	
	'''
	python支持运算符重载
	__init__ : 构造函数，在生成对象时调用
	__del__ : 析构函数，释放对象时使用
	__repr__ : 打印，转换
	__setitem__ : 按照索引赋值
	__getitem__: 按照索引获取值
	__len__: 获得长度
	__cmp__: 比较运算
	__call__: 函数调用
	__add__: 加运算
	__sub__: 减运算
	__mul__: 乘运算
	__truediv__: 除运算
	__mod__: 求余运算
	__pow__: 乘方
	'''
	def __str__(self):
		return '__str__'
	
	def __add__(self, other):
		return '__add__'


x = MyClass('hhho')
print(x.i)
print(x.f())
print(x.name)
# print(x.__age)
# print(x.__privatefunc()) # 私有方法无法在外部直接访问
print('=====================')
y = MyClass('world')
print(y.i)
print(y.f())
print(y.name)
x.i += 1
print(x.i) #对象属性
print(y.i) #对象属性
print('=========类属性============')
print(MyClass.i) #类静态变量
print(MyClass.name)
# print(MyClass.f()) #python无静态方法

'''
python标准库：
	os
	shutil
	glob
	sys
	re
	math
	random
	urllib
	datetime
	zlib
	timeit
	doctest
'''