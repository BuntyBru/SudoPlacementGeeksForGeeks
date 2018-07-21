n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    arr2 = []
    for j in range(n1-1):
        if arr[j] > max(arr[j+1:]):
            arr2.append(arr[j])
    arr2.append(arr[n1-1])
    print(*arr2)
    
    