#n1 = 7
#arr=[1,2,3,5,6,8,9]
# 4
# [1,3,6,7]
n = int(input())
for  i in range(n):
    item = [int(x) for x in input().split()]
    n1 = item[0]
    num = item[1]
    arr = [int(x) for x in input().split()]
    min =100000000
    t=0
    for i in range(n1):
        if num > arr[i]:
            m = num-arr[i]
            if m <= min:
                min= m
                t=0
        else:
            m = arr[i]-num
            if m <= min:
                min=m
                t=1
			

    if t == 1:
    	print(num+min)
    else:
    	print(num-min)
        