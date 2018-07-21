n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    arr.reverse()
    arr1= []* n1
    arr1.append(arr.pop())
    while arr != []:
        arr1.append(arr.pop())
        if len(arr) !=0:
            arr1.insert(0,arr.pop())
    print(*arr1)