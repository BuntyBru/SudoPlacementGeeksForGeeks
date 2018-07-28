#code
arr = ['a','e','i','o','u']
n = int(input())
for i in range(n):
    a  = input()
    ans =[]
    array=[]
    l = []
    for i in range(len(a)):
    	ans.append(a[i])
    	l.append(a[i])
    	if a[i] in arr:
    		array.append(i)

    for i in range(len(array)):
    	ans[array[i]] = l[array[len(array)-1-i]]
	
	
    print(*ans,sep="")