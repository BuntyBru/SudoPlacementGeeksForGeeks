#code
arr = ['a','e','i','o','u','A','E','I','O','U',' ']
n = int(input())
for i in range(n):
    inp = input()
    ans=[]
    for i in range(len(inp)):
        if inp[i] in arr:
            ans.append(inp[i])
    if len(ans) > 0:
        print(*ans, sep='')
    else:
        print("No Vowel")
    
