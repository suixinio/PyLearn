import os
os.chdir('D:\\Workspace\\PyLearn')#改变路径
list1 = os.listdir()#将文件夹中的文件放入list中


for i in list1:
    #print(i)
    print(i,os.path.getsize(i))
