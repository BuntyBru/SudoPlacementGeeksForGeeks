
n = int(input())

for i in range(n):
    n1 =[int(x) for x in input().split()]
    lengthofArr = n1[0]
    rotate = n1[1]
    arr =[int(x) for x in input().split()]
    print(*arr[rotate:]+arr[:rotate])