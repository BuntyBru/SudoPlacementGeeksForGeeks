n=int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    ans= []
    arr.append(9999999)
    for j in range(n1):
        if arr[j] > arr[j+1]:
            ans.append(arr[j+1])
        else:
            ans.append(-1)
    print(*ans)
    