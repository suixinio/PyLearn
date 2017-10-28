# 递归采用分制思想

def feibonaqie(x):
    first =1
    second =1
    sum = 0
    for i in range(2,x):
        sum= first + second
        first = second
        second = sum
        i+=1
    return sum

def fab(n):
    n1 =1
    n2 =1
    n3 =1

    if n<1:
        print("输入有问题")
        return -1
    while(n-2)>0:
        n3  = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3

def diguifeibo(x):
    #if x == 1:
     #   return 1
    #if x == 2:
    #    return 1
    if x==1 or x == 2:
        return 1
    
    return diguifeibo(x-1)+diguifeibo(x-2)


print(feibonaqie(20))
print(diguifeibo(20))
print(fab(20))
