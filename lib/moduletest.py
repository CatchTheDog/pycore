import sys
print(sys.path)

'''
可以使用__name__属性判断是否是当前模块自身在运行
'''
if __name__ == '__main__':
	print('程序自身在运行')
else:
	print('被引入时执行')

