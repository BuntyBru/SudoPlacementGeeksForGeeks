class Queue:
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        self.items.pop()
    def __str__(self):
        return str(self)
        
def rotten(grid,r,c):
    t = 0
    row= Queue()
    column = Queue()
    time = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                row.enqueue(i)
                column.enqueue(j)
                time.append(t)
    finalt=[]
    while not row.isEmpty() and not column.isEmpty() and len(time)!=0:
        newi=row.dequeue()
        newj=column.dequeue()
        newt = time.pop()
        
        if newi+1<r and grid[newi+1][newj] == 1:
            grid[newi+1][newj]=2
            row.enqueue(newi+1)
            column.enqueue(newj)
            time.insert(0,newt+1)
            finalt.append(newt+1)
        
        if newj+1 < c and grid[newi][newj+1] == 1:
            grid[newi][newj+1]=2
            row.enqueue(newi)
            column.enqueue(newj+1)
            time.insert(0,newt+1)
            finalt.append(newt+1)
            
        if newi-1 >=0 and grid[newi-1][newj] ==1:
            grid[newi-1][newj] =2
            row.enqueue(newi-1)
            column.enqueue(newj)
            time.insert(0,newt+1)
            finalt.append(newt+1)
        
        if newj-1 >=0 and grid[newi][newj-1] == 1:
            grid[newi][newj-1] =2
            row.enqueue(newi)
            column.enqueue(newj-1)
            time.insert(0,newt+1)
            finalt.append(newt+1)
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                return -1
    
    return max(finalt)
            
        
                

n = int(input())
for i in range(n):
    item = [int(x) for x in input().split()]
    r = item[0]
    c = item[1]
    inp = [int(i) for i in input().strip().split()]
    grid = []
    for i in range(0, len(inp), c):
        grid.append(inp[i:i + c])
    
    ans = rotten(grid,r,c)
    print(ans)
    