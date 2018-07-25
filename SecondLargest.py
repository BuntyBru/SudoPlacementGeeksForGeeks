#code
n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    k = max(arr)
    arr.pop(arr.index(k))
    print(max(arr))