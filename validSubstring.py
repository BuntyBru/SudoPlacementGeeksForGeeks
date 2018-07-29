class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def Push(self,item):
        self.items.append(item)
    def Pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self)
n = int(input())
for i in range(n):
    arr = input()
    s = []
    s.append(-1)
    count =0
    for i in range(len(arr)):
        if arr[i] == '(':
            s.append(i)
            print("in if condition ",s)
            
        else:
           s.pop()
           print("In else condition ",s)
           if len(s) !=0:
               count = max(count, i - s[len(s)-1])
           else:
               s.append(i)
                
    print(count)    
        