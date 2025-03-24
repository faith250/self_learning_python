def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b= b,a+b
    print()

fib(200)
fib(0)
print(fib(0))

#print a list rather than print the sequence 
def fib(n):
    result=[]
    a,b=0,1
    while a<n:
        #print(a,end=' ')
        result.append(a)
        a,b= b,a+b
    return result

f=fib(3)
print(f)

