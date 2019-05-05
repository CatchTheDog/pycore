import random
'''
列表推导式 从序列创建列表的简单途径
'''

vec1 = [2,4,5]
vec2 = [6,7,8,9,10]
print([3*x for x in vec1 if x > 3])
print([[x,x**2] for x in vec1])
print([x*y for x in vec1 if x > 3 and x < 5 for y in vec2 if y%2 == 0])
print([vec1[i]*vec2[i] for i in range(len(vec1))])

'''
根据CPU信息，内存信息，磁盘信息生成随机数
'''
def random():
	pass

'''
数组嵌套——矩阵
'''
def initMatrix(func):
	matrix = []
	for i in range(4):
		temp = []
		for j in range(5):
			temp.append(func(i,j))
		matrix.append(temp)
	return matrix
'''
矩阵乘法 点乘
'''
def matrixMultiplication(matrixA,matrixB):
	if len(matrixA) < 0 or len(matrixB) < 0:
		pass

'''
将矩阵按照行划分
'''
def matrixTransposition(matrix):
	if len(matrix) <=0:
		raise Exception
	else:
		pass

'''
数据结构遍历
字典遍历：items()
列表遍历：enumerate()
遍历两个或多个序列:zip()
反向遍历一个序列:reversed()
顺序遍历:sorted()
'''
knights = {'a':1,'b':2,'c':3}
for k,v in knights.items():
	print(k,'->',v)

for i,v in enumerate(['a','b','c']):
	print(i,'->',v)

array1 = ['a','b','c','d']
array2 = ['i','x','a','c']
for x,y in zip(array1,array2):
	print('first element %s,second element %s'%(x,y))

for i in reversed(array1):
	print(i)

for j in sorted(array2):
	print(j)
