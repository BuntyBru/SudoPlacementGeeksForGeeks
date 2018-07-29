n1 = 4
arr = [4,3,2,6]
start = 0
end = 1
ans =[]
sum1 = 0
t =1 
while len(arr) != 1:
    arr.sort()
    sum1 = arr[start] +arr[end]
    arr.append(sum1)
    ans.append(sum1)
    arr.pop(0)
    arr.pop(0)
    
print(sum(arr))