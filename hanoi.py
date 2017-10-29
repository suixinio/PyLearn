def hanoi(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前N-1个盘子从X移动Y上
        print(x,'-->',z)
        hanoi(n-1,y,x,z)#将Y上的n-1歌盘子移动到z上

n = int(input('请输入汉诺塔的层数：'))
hanoi(n,'x','y','z')
