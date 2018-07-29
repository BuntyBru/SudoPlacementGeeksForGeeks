#code
def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

n = int(input())
for i in range(n):
    n1 = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    st =[]
    st2=[]
    for i in range(n1):
        if i % 2 == 0:
            st.append(arr[i])
        else:
            st2.append(arr[i])
    num1 = magic(st)
    num2= magic(st2)
    print(num1+num2)