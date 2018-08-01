#code

n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [x for x in input().split()]
    arr2 = list(set(arr))
    #print(arr2)
    count=[0]*len(arr2)
    if len(arr) == len(arr2):
        arr2.sort()
        #print(arr2[0])
    else:
        for i in range(len(arr)):
            if arr[i] in arr2:
                count[arr2.index(arr[i])] = 1 + count[arr2.index(arr[i])]
        #print(count)
        maximum = max(count)
        answer =[]
        
        for i in range(len(count)):
            if count[i] == maximum:
                answer.append(arr2[i])
        
        answer.sort()
        print(answer[0])
                