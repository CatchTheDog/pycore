import math
import cmath
import random

print('当前范围内的变量、方法和定义的类型列表：',dir())


def dirs(modules):
	print('math 模块中定义的方法：')
	funcs = dir(modules)
	for index in range(len(funcs)):
		print(funcs[index])


dirs(math)
dirs(cmath)

#数学函数
print(abs(-10))
print(math.ceil(1.2))
print(math.floor(1.7))
print(math.exp(4))
print(math.log(100,10))
print(max(1,4,5))
print(min(23,45))
print(pow(2,3))
print(round(1.3234544585,6))
print(math.sqrt(4))

#随机函数
print(random.choice(range(2,200,5)))
print(random.randrange(2,200,5))
print(random.random())
random.seed(10)
print(random.random())
r = range(10) #python3 中range()返回一个可遍历对象，而不是一个列表
p = [1,2,3,4,5,6]
random.shuffle(p)
print(p)
print(random.uniform(12,15))

#常数
print(math.pi)
print(math.e)