'''
f1 = open('D:/record.txt')
index = 1
f_boy = open('D:/boy_'+str(index)+'.txt','x')
f_girl = open('D:/girl_'+str(index)+'.txt','x')
for say in f1:
    #print(say.rfind('='))
    if say.rfind('=') != -1:
        print(index)
        index+=1
        f_boy.close()
        f_girl.close()
        f_boy = open('D:/boy_'+str(index)+'.txt','x')
        f_girl = open('D:/girl_'+str(index)+'.txt','x')
    else:
        if say.rfind("小甲鱼",0,say.index(':')) !=-1:
            print(say.rfind("小甲鱼",0,say.index(':')))
            f_boy.write(say[say.index(':')+1:])
            f_boy.flush()
        elif say.rfind("小客服",0,say.index(':'))!=-1:
            f_girl.write(say[say.index(':')+1:])
            f_girl.flush()
            
f_boy.close()
f_girl.close()
'''


def save_file(boy,girl,count):
    file_name_boy = 'D:/boy_'+str(count)+'.txt'
    file_name_girl = 'D:/girl'+str(count)+'.txt'
    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    
    f1 = open('D:/record.txt')

    boy = []
    girl = []
    count = 1

    for each_line in f1:
        if each_line[:1] != '=':
            # 这里进行字符串分割操作
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            # 文件的分别保存工作
            save_file(boy,girl,count)

            boy = []
            girl = []
            count+=1

    save_file(boy,girl,count)

    f1.close()
    
split_file('')
