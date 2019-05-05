import math
import pickle
import pprint
'''
输入输出测试
python有两种输出值的方式：表达式语句和print()函数
还可以使用文件对象的write()方法，标准输出文件可用sys.stdout引用
可以用str.format(),repr(),str()进行格式化
'''
s = 'xyz,hoo!'
print(str(s))
print(repr(s))

for x in range(1,11):
	print(repr(x).rjust(2),repr(math.pow(x,2)).rjust(3),end=' ')
	print(repr(math.pow(x,3)).rjust(4))

for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

'''
标准输入
'''
str = input('请输入:')
print('你输入的内容是:',str)


f = open('./tmp/foo.txt','w+',encoding='utf-8')
f.write('Python 是一个非常好的语言.\n是的，的确非常好！')
f.close()

f = open('./tmp/foo.txt','r+',encoding='utf-8')
# y = f.read()
# y = f.readline()
# y = f.readlines()
for line in f:
	print(line,end='')
# print(y)
print(f.tell(),':')
f.close()

'''
使用with,file.seek()
'''
with open('./tmp/foo.txt','rb+') as f:
	f.write(b'012345678abcdef')
	f.seek(-5,2)
	print(f.read())


'''
pickle模块实现了序列化和反序列化
'''
data1 = {'a':[1,2,3,4+2j],'b':('string',u'Unicode String'),'c':None}
selfref_list = [1,2,3]
selfref_list.append(selfref_list)
with open('./tmp/data.pk1','wb') as output:
	pickle.dump(data1,output)
	pickle.dump(selfref_list,output,-1)

with open('./tmp/data.pk1','rb') as input:
	data_1 = pickle.load(input)
	pprint.pprint(data_1)
	data_2 = pickle.load(input)
	pprint.pprint(data_2)