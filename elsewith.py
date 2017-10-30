'''
丰富的else语句

1、要么怎么样，要么不怎么样
2、干完了怎么样，干不完就别想怎么样
3、没问题，那就干吧

'''
#2
def showMaxFactor(num):
    count = num//2
    while count > 1:
        if num % count == 0:
            print('%d最大的约数是%d'%(num,count))
            break
        count -=1
    else:
        print('%d是素数',% num)


#3
try:
    print(int('abc'))
except ValueError as reason:
    print('出错啦：'+str(reason))
else:
    print('没有任何异常')


'''
with 语句
文件中使用with语句，自动考虑关闭文件
'''
try:
    with open('data.txt') as f:
        for each_line in f :
            print(each_line)
except OSError as reason:
    print('出错啦')
