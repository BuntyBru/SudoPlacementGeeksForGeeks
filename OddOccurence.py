#code
import collections
n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    ctr = collections.Counter()
    for i in range(n1):
        ctr[arr[i]] = 1+ ctr[arr[i]]
    #print(ctr)
    k = list(ctr.values())
    l = list(ctr.keys())
    ans =-1
    for i in range(len(k)):
        if k[i]%2 !=0:
           ans = i 
    print(l[ans])
            