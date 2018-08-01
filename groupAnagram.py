n1 = int(input())
for i in range(n1):
    n = int(input())
    arr = list(input().split())
    h = {}
    
    for i in range(len(arr)):
        word = "".join(sorted(arr[i]))
        if word in h:
            h[word] += 1
        else:
            h[word] = 1
            
    for val in sorted(h.values()):
        print(val, end = " ")
    print()