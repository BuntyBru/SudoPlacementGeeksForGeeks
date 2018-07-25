#code
n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    item = int(input())
    if item in arr:
        print(arr.index(item))
    else:
        print(-1)