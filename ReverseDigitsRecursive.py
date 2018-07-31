#code
def rev(n, res=0):
    if n == 0:
        return res
    res = (res*10)+n%10
    return rev(n//10, res)

n = int(input())
for i in range(n):
    n1 = int(input())
    print(rev(n1))
    
    