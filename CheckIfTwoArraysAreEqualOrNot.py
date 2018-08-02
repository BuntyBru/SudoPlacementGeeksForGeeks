#code
n = int(input())
for i in range(n):
    n1 = int(input())
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        print(1)
    else:
        print(0)