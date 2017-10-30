import os
def findfile(path,file_name,list2):
    #os.chdir(path)
    list1 = os.listdir(path)
    #print(path)
    for i in list1:
        #print(i,'|',os.path.isdir(os.getcwd()+'/'+i))
        if os.path.isdir(path+'\\'+i):
            #print(1)
            findfile(path+'\\'+i,file_name,list2)
        else:
            if i == file_name:
                list2.append(path+'\\'+file_name)
                return list2
                #print(path+'\\'+file_name)

            
def findtxtfile(path,list2):
    list1 = os.listdir(path)
    #print(path)
    for i in list1:
        if os.path.isdir(path+'\\'+i):
            findfile(path+'\\'+i,file_name,list2)
        else:
            if (os.path.splitext(i))[1] == '.txt':
                list2.append(path+'\\'+i)
                return list2



    
def writefile(data,path):
    f = open(path+'\\'+'vedioList.txt','w')
    for i in data:
        f.writelines(i+os.linesep)
    f.flush()
    f.close()


#path1 = input('请输入待查找的初始目录：')
#file_name = input('请输入查找的目标文件：')

path1='D:\\Workspace\\PyLearn\\find'
file_name='a.txt'
list1 = []

if os.path.exists(path1):
    #得到相关格式的文件
    list1 = findfile(path1,file_name,list1)
    print(list1)
    #writefile(list1,path1)
else:
    print('输入目录有误')
