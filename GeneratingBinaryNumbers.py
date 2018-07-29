#code
class Queue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []
    
    def Enqueue(self,item):
        self.items.insert(0,item)
    
    def Dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
        
        
def generateBinary(n,ans):
    q = Queue()
    q.Enqueue('1')
    while n > 0:
        n = n-1
        s1 = q.Dequeue()
        ans.append(s1)
        s2 = s1
        q.Enqueue(s1+'0')
        q.Enqueue(s2+'1')
    
    print(*ans)

n = int(input())
for i in range(n):
    it = int(input())
    ans = []
    generateBinary(it,ans)