try:
    sum = 1+'1'
    f=open('我为什么是一个文件.txt')
    print(f.read())
except OSError as reason:
    print('文件不存在',reason)
except TypeError as reason:
    print('类型出错了',reason)
finally:
    f.close()
