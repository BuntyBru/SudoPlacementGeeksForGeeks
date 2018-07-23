def countDistinct(arr, n, k):
    # Code here
    arr2=[]
    ans=[]
    while len(arr) > k-1:
        for i in range(k):
            arr2.append(arr[i])
        ans.append(len(set(arr2)))
        arr.pop(0)
        arr2=[]
    print(*ans)