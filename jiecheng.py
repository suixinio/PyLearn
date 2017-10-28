def factorial_1(x):
    sum  =1;
    for i in range(1,x):
        sum*=i
    return sum

def factorial_2(x):
    if x == 1:
        return 1
    return x*factorial_2(x-1)

print(factorial_1(5))
print(factorial_2(5))
