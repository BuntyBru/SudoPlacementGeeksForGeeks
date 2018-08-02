#code
n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())
    h = {}
    l=list(set(arr))
    count=0
    for i in range(n1):
        h[arr[i]] = True
    arr.sort()
    arr.reverse()
    for i in range(n1):
        x = arr[i]
        if abs(x-k) in arr[i+1:] and h[abs(x-k)]:
            count = count+1
        
        h[x] = False
    #print(h)
    print(count)
        