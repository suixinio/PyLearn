import os
os.chdir('D:\\Workspace\\PyLearn')#改变路径
list1 = os.listdir()#将文件夹中的文件放入list中

dirct1 = dict()

list2 = []
for i in list1:
    name = os.path.splitext(i)
    if name[1] not in dirct1:
        dirct1[name[1]] = 1
    else :
        dirct1[name[1]] = dirct1[name[1]]+1

for key,value in dirct1.items():
    print('后缀为：%s，出现：%s次'%(key,value))
