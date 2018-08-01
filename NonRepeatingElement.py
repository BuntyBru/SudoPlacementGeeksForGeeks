n = int(input())
for i in range(n):
    n1 = int(input())
    arr =[int(x) for x in input().split()]
    ans =[]
    for i in range(len(arr)):
        if arr[i] not in arr[i+1:]:
            ans.append(arr[i])
    if len(ans) >0:
        print(ans[0])
    else:
        print(0)


