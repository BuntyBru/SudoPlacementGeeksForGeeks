n = int(input())

for i in range(n):
    n1 = int(input())
    arr= [int(x) for x in input().split()]
    finalarr=[]
    arr1=[]
    rotate = int(input())
    
    while len(arr) >rotate:
            for  j in range(rotate):
                arr1.insert(0,arr.pop(0))
            finalarr = finalarr+arr1
            arr1=[]
        
    arr= arr[::-1]
    finalarr = finalarr+arr
    print(*finalarr)
    