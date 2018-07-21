n = int(input())
for i in range(n):
    n1 = int(input())
    arr=[int(x) for x in input().split()]
    n2 = int(input())
    
    t = []
    t = arr[n2:] + arr[:n2]
    arr=t
    print(*arr)
        