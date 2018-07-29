#code
n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())
    ans =[]
    start = 0
    end = k
    while len(arr) > k-1:
        
        for i in range(start,end):
            if arr[i] < 0:
                kt = arr[i]
                break
            else:
                kt=0
        ans.append(kt)
        kt=0
        arr.pop(0)
        
    print(*ans)
       