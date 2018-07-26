#code
n = int(input())
for i in range(n):
    item = [int(x) for x in input().split()]
    n1 = item[0]
    k = item[1]
    arr = [int(x) for x in input().split()]
    arr2 = []
    max = 0
    for i in range(n1):
        if arr[i] <= k and arr[i] > max:
            max = arr[i]
            
            arr2.append(i)
        
    if len(arr2) > 0:
        print(arr2.pop())
    else:
        print(-1)
            
            