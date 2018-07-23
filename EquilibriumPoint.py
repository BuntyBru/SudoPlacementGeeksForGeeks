#code

n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    ans = -1
    key=0
    if n1 ==1:
        print(1)
    
    if n1 == 2:
        print(-1)
    
    else:
        arr2 = []
        arr2.append(arr.pop(0))
        while len(arr)>0:
            if sum(arr2) == sum(arr)-arr[0]:
                ans = len(arr2) +1
                arr = []
                key =1
                break
            else:
                arr2.append(arr.pop(0))
                key = 2
        if key ==1:
            print(ans)
        if key ==2:
            print(-1)
                