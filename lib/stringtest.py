import sys
#字符串运算
'''
+ * [] [:] in    not in    r/R    %
'''

print(r'\n') #原始字符串
for x in 'hello':
	print(x)

print('我叫%s,今年%d岁！'%('小明',10)) #字符串格式化

#字符串内建函数
print('hello'.capitalize().center(30,'-').count('-'))

r = ('1','3','4','54','5')
print('-'.join(r))

#集合
basket = {'apple','orange','apple','pear'}
a = set('abcgdddd')

print(a)
a.add('f')
print(a)
a.clear()


#迭代器 iter() next()
list = [1,2,3,4]
it = iter(list)
for index in range(len(list)):
	print(next(it))


'''
把一个类作为一个迭代器使用需要在类中实现以下两个方法：
__iter__()
__next__()
'''
class MyNumbers:
	def __iter__(self):
		self.a = 1;
		return self;
	
	def __next__(self):
		x = self.a
		self.a += 1
		return x


myClass = MyNumbers()
myiter = iter(myClass);
for index in range(5):
	print(next(myiter))



'''
在python中，使用了yield的函数被称为生成器.
生成器返回一个迭代器的函数，只能用于迭代操作
在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值；并在下一次执行next()方法时从当前位置继续
'''

def fibonacci(n):
	a, b, counter = 0, 1, 0
	while True:
		if(counter>n):
			return
		yield a
		a, b = b, a+b
		counter += 1

f = fibonacci(10)

while True:
	try:
		print(next(f),end=" ")
	except StopIteration:
		sys.exit()

