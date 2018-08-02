#code
n= int(input())
for i in range(n):
    item = [int(x) for x in input().split()]
    size1 = item[0]
    size2 = item[1]
    
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    ctr=0
    for i in arr2:
        if i in arr1:
            ctr=ctr+1
    if ctr == size2:
        print("Yes")
    else:
        print("No")