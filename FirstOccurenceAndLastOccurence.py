#code
n = int(input())
for i in range(n):
    n1 = int(input())
    arr= [int (x) for x in input().split()]
    num = int(input())
    arr2=[]
    for i in range(n1):
        if arr[i] == num:
            arr2.append(i)
    
    if len(arr2) >= 1:
        print(arr2[0], arr2[len(arr2)-1])
    if len(arr2) < 1:
        print(-1)

        