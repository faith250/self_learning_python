def fib(n):
    result=[]
    a,b=0,1
    while a<n:
        #print(a,end=' ')
        result.append(a)
        a,b= b,a+b
    return result

print(fib(500))

