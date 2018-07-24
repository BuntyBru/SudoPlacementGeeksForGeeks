def function(num):
    arr2 = []
    while num > 0:
        temp = num %10
        num = (num-temp)//10
        arr2.append(temp)
        count=0
    
    for i in range(len(arr2)-1):
        if arr2[i]- arr2[i+1] ==1 or arr2[i] - arr2[i+1] == -1:
            count = count+1
    if count == len(arr2)-1:
    	return True
    else:
    	return False

n = 8
k= 54
arr= [7,98,56,43,45,23,12,8]
ans=[]
for i in range(n):
	if arr[i] < k:
		if arr[i] < 10:
			ans.append(arr[i])
		else:
			t = function(arr[i])
			if t:
				ans.append(arr[i])
print(ans)