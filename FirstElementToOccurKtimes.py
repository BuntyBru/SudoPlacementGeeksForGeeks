import collections 
for i in range(int(input())):
    item = [int(x) for x in input().split()]
    n = item[0]
    k = item[1]
    l=list(map(int,input().split()))
    p= collections.Counter(l)
    #print(p)
    final=-1
    for i in l:
        if p[i]==k:
            final=i
            break
    
    
    
    print(final)
        