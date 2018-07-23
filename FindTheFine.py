
n = int(input())
for i in range(n):
    item = [int(x) for x in input().split()]
    n1 = item[0]
    date = item[1]
    arr = [int(x) for x in input().split()]
    arr2 =[int(x) for x in input().split()]
    sum=0
    if date%2 ==0:
        for i in range(n1):
            if arr[i] % 2!=0:
                sum = sum + arr2[i]
        
    else:
        for i in range(n1):
            if arr[i] % 2 ==0:
                sum = sum + arr2[i]
    
    print(sum)