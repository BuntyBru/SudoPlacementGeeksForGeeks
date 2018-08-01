#code
n = int(input())
for i in range(n):
    string1 = input()
    string2 = input()
    one = len(string1)
    two = len(string2)
    count=[]
    
    for i in range(one):
        if string1[i] in string2:
            count.append(i)
    if len(count) == 0:
        print("No character present")
    else:
        print(string1[count[0]])