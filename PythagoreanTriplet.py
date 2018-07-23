

#n1 = 44
#arr = [68,35,1,70,25,79,59,63,65,6,46,82,28,62,92,96,43,28,37,92,5,3,54,93,83,22,17,19,96,48,27,72,39,70,13,68,100,36,95,4,12,23,34,74]
#n1 = 5
#arr= [6,7,8,9,10]

n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x)**2 for x in input().split()]
    arr.sort()
    key=0
    while len(arr) > 1:
        k=arr.pop(0)
        for i in range(len(arr)):
            if k+arr[i] in arr:
                print("Yes")
                arr=[]
                key=0
                break
            else:
                key=2
    if key ==2:
        print("No")

        