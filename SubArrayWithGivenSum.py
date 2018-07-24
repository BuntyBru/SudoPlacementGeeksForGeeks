n = int(input())
for i in range(n):
    item = [int(x) for x in input().split()]
    n1 = item[0]
    k = item[1]
    key = 0
    arr = [int(x) for x in input().split()]
    arr2=[]
    ans=[]
    sum=0
    key=0
    while len(arr) > 0:
        for i in range(len(arr)):
            sum= sum +arr[i]
            
            if sum == k:
                ans.append(len(arr2)+1)
                ans.append(i+len(arr2)+1)
                key=1
                arr=[]
                break
        if sum != k:
            arr2.append(arr.pop(0))
            sum=0
            key=2
    if key ==1:
        print(*ans)
    if key ==2:
        print(-1)