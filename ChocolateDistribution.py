
#arr=[17,83,59,25,38,63,25,1,37]
#arr=[34,88,89,39,67,71,85,57,18,7,61,50,38,6,60,18,19,46,84,74,59]
#arr=[6,83,23,83,18,31,94,75,27,94,87,54,44,75,15,14,80,78,63]

#code
n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    child = int(input())
    arr.sort()
    minArray = []
    if n1 != child:
        if n1 == 1:
            minArray.append(0)
        if n1 == 2:
            minArray.append(arr[1]-arr[0])
        else:
            while len(arr) > child-1:
                minArray.append(arr[child-1]-arr[0])
                arr.pop(0)
    if n1 == child:
        minArray.append(max(arr)-min(arr))
    #t = min(minArray)
    print (min(minArray))