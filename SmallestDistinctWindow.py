t = int(input())
while t:
    s=input().strip()
    l=len(s)
    mincount=100001
    
    #Calculate Total distinct character
    s1=set(list(s))
    total=len(s1)
    
    # dict to store last occurance of char
    LastOccOfChar={}
    count=0
    for i in range(l):
        if s[i] not in LastOccOfChar:
            count+=1
        LastOccOfChar[s[i]]=i
        #print("The last occurence ",LastOccOfChar)
        if total==count:
            m=0
            for j in range(l):
                if LastOccOfChar[s[j]]==j:
                    m=j
                    break
            mincount=min(mincount,i-m+1)
    
    print(mincount)
    t-=1