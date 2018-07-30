#code

n = int(input())
for i in range(n):
    n1 = int(input())
    arr= [int (x) for x in input().split()]
    max_curr = -999999
    max_forever = 0
    
    for i in range(n1):
        max_forever = max_forever + arr[i]
        if max_forever > max_curr:
            max_curr = max_forever
        if max_forever < 0:
            max_forever =0
    print(max_curr)
    