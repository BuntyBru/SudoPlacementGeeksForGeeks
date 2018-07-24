n = int(input())
for i in range(n):
    n1 = int(input())
    arr=[int(x) for x in input().split()]
    arr2=[]
    ans=[]
    ans.append(max(arr))
    for j in range(n1-1):
        if arr[j] > arr[j+1]:
            arr2.append(1)
        if arr[j] < arr[j+1]:
            arr2.append(-1)
    if arr2.count(1) == 0:
        ans.append(1)
        print(*ans)
    if arr2.count(-1) == 0:
        ans.append(2)
        print(*ans)
    if arr2.count(1) !=0 and arr2.count(-1) !=0:
        
        if arr2.count(1) < arr2.count(-1):
            ans.append(4)
            print(*ans)
        if arr2.count(1) > arr2.count(-1):
            ans.append(3)
            print(*ans)