n = int(input())
for i in range(n):
    item = [int(x) for x in input().split()]
    n1 = item[0]
    k = item[1]
    
    arr= [int(x) for x in input().split()]
    arr2=[]
    ans=[]
    while len(arr) > k-1:
        arr2=[]
        for i in range(k):
            arr2.append(arr[i])
           
        ans.append(max(arr2))
        arr.pop(0)
        
    print(*ans)