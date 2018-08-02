T = int(input())
for i in range(T):
    inds = []
    N = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    hash = {}
    for i in range(N):
        sum += arr[i]
        if sum == 0:
            inds.append([0, i])
        if hash.get(sum) != None:
            for j in hash[sum]:
                inds.append([j + 1, i])
            hash[sum].append(i)
        else:
            hash[sum] = [i]
    print(hash)
    print(inds)
    print(len(inds))