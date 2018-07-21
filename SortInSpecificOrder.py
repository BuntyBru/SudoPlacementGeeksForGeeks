#2
#7
#1 2 3 5 4 7 10
#7
#0 4 5 3 7 2 1


n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    
    arr2 = []
    arr3 =[]
    for i in range(n1):
        if arr[i] %2 != 0:
            arr2.append(arr[i])
        else:
            arr3.append(arr[i])
            
        arr2.sort()
        arr2.reverse()
        arr3.sort()
        
    print(*arr2+arr3)