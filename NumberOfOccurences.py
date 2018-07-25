n = int(input())
for i in range(n):
    item = [int (x) for x in input().split()]
    n1 = item[0]
    k = item[1]
    arr = [int(x) for x in input().split()]
    if k in arr:
        print(arr.count(k))
    else:
        print(-1)