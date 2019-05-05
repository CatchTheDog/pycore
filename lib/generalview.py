#python 3 默认使用UTF8编码脚本文件
print("你好，世界")

'''python中变量赋值不需要声明，使用前必须赋值，可同时为多个变量赋值，也可为多个对象指定多个变量
   可以使用del var 删除一些对象的引用
   有五个标准的数据类型：
		Numbers(数字):
			int-有符号整型 0x69 -0490 10
			long-长整型 123L -0x123L -0123L
			float-浮点型 0.0 8.1e-10
			complex-复数 3.14j .876j -.123-9j 12.j
		String(字符串)
		    字符串: R   U   N   O   O   B
		    索  引: 0   1   2   3   4   5
		    索  引:-6  -5  -4  -3  -2  -1
		List(列表)
		Tuple(元组)
		Dictionary(字典)
		Set(集合)
'''

#获取子串，重复字符串，拼接字符串
s = 'abcdef'
print(s[0:2]*3+'@'+s[0:-2:2])

s = ' \rtestMethodInPython3String \r'
#print(s.strip())
#print(s.strip('t'))

#list
list = ['runoob',786,2.23,'john',1,3+1.2j]
tinyList = ['a','b']
print(list)
print(list[1])
print(list[1:-1])
print(list*2)
print(list+tinyList)

#元组 操作同list,不过元组不可二次赋值，相当于只读列表
t = ('runoob',786,2.23,'john',1,3+1.2j)
tinyTyple = ('a','b')

#字典 无序的对象集合
d = {}
d['one'] = 'This is one'
d[2] = 'This is two'

tinyDict = {'name':'john','1':'2'}
print(d['one'])
print(d[2])
print(tinyDict)
print(tinyDict.keys())
print(tinyDict.values())


#数据类型转换 将4进制数字转换为10进制
print(int('123',4))
print(repr(tinyDict))
print(complex(1,2))
print(eval('pow(2,2)'))
print(tuple({1:2,3:4}))


x = set('runoob')
y = set('google')
print(x,y)
print(x|y)
print(x&y)
print(x-y)

#创建元组
print(dict(a=1,b=2,c=3))
#不可变集合
print(frozenset(range(10)))
print(chr(123))
print(ord('{'))
print(hex(123))
print(oct(123))
print(bin(123))

print(5//2)

a = 2
b = 4
print(a&b)

'''
+ - * / % ** //
== != <> > < >= <=
= += -= *= /= %= **= //=
& | ^ ~ << >>
and or not
in   not in
is   is not
'''


print(bin(-4))
print(bin(-4>>5))

#if
flag = False
name='python'
if name == 'python':
	flag = True
	print('hhhh')
elif name == 'java':
	print('llll')
elif name == 'c':
	print('cccc')
else:
	pass



#while
count = 0
while count < 5:
	print(count , '  is less than 5')
	count+=1
else:
	print(count ,' is not less than 5')


#for
for letter in 'python':
	print('当前字母:',letter)

fruits = ['banana','apple','mango']
for fruit in fruits:
	print('当前水果:',fruit)

for index in range(len(fruits)):
	print('当前水果:',fruits[index])