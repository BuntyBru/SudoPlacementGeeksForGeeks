n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    s = list(set(arr))
    s.sort()
    #print(s)
    count=0
    for i in range(len(s)-1):
        #print(abs(s[i] - s[i+1]))
        if abs(s[i] - s[i+1]) == 1:
            count = 1+count
    if count == len(s)-1:
        print("Yes")
    else:
        print("No")
    