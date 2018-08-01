n1 = int(input())
for i in range(n1):
    n=list(input())
    l=[int(n[0])]
    d=[]
    flag=0
    for j in range(1,len(n)):
        if n[j].isdigit():
            l.append(l[j-1]*int(n[j]))
    for j in range(len(n),0,-1):
        for k in range(len(n)-j, -1,-1):
            if k+j-1>=0 and k+j-1<=len(l)-1:
                m=l[k+j-1]
                if k!=0:
                    m= (m/l[k-1])
                if m not in d:
                    d.append(m)
                else:
                    flag=1
                    break
        if flag==1:
            break
    if flag==1:
        print(0)
    else:
        print(1)
