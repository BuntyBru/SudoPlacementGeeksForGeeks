#code
def foo(num,n1):
    if num > 0:
        foo(num-5,n1)
        print(num,end=" ")
        
    if num <= 0:
        #print(num)
        foo2(num,n1)
    
def foo2(num,n1):
    
    if num <= n1:
        t = num+5
        foo2(t,n1)
        print(num,end=" ")
    
    
n = int(input())
for i in range(n):
    n1 = int(input())
    foo(n1,n1)
    print()