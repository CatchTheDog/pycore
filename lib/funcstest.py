import math
import builtins

'''
函数定义练习
参数： 必须参数
	  关键字参数
	  默认参数      age,如果不传入此参数，则使用默认值
	  不定长参数
'''
def func(str,name,age=20):
	if str != '':
		return str%(name,age);
	else:
		raise Exception('arguments str can not be null.')

print(func(r'我是%s,我今年幼儿园毕业才%d年，请不要和我计较.','马云',50))

'''
pass 占位作用
'''
def func_1():
	pass

func_1()

'''
不定长参数   *前导的参数   以元组的形式导入，存放所有未命名的变量参数
            **前导的参数  以字典的形式导入，调用时以关键字的形式传入
'''
def func_2(arg1,*vartuple,**vardict):
	s = set(vartuple);
	s.add(arg1)
	s1 = set(vardict.values())
	s.union(s1)
	print(s)


func_2(1,3,4,5,5,55,a=1,b=3)

'''
*可单独出现，但是其后参数必须以关键字参数传入
'''
def func_3(a,*,c):
	print(a,c)


func_3(1,c=4)

'''
匿名函数：使用lamda来创建匿名函数
'''

sum = lambda arg1, arg2: arg1 + arg2

print(sum(1,2))


'''
python变量作用域：
	L Local  局部作用域
	E Enclosing 闭包函数外的函数中
	G Global 全局作用域
	B Built-in 内置作用域——内置函数所在模块的范围
变量查找以L->E->G->B的顺序进行

python中只有模块(module),类(class)以及函数(def,lamda)才会引入新的作用域
可以使用global和nolocal关键字在内部作用域中修改外部作用域的变量
'''

print(dir(builtins)) #内置作用域是用builtin 的标准模块来实现的，需要引入

def outer():
	num = 10
	def inner():
		nonlocal num #将num引用指向闭包中的变量num
		num = 100
		print(num)
	inner()
	print(num)

outer()

a = 10
def test():
	global a #将a引用指向全局变量a
	a += 1
	print(a)
test()