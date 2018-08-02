#code
n = int(input())
for i in range(n):
    item = [x for x in input().split()]
    a=int(item[0])
    b =int (item[1])
    h={}
    ans = []
    for i in range(a,b+1):
        l = list(str(i))
        k = set(l)
        if len(l) == len(k):
            ans.append(i)
    print(*ans)
        