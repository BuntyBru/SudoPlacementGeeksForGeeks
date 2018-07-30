{
#Initial Template for Python 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        pos = int(input())
        deleteNode(llist.head, pos)
        llist.printList(llist.head)
# Contributed by: Harshit Sidhwa
                               
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
# Your task is to complete this function
# function should just delete the Node
# function shouldn't print or return any data
def deleteNode(head, x):
    count=1
    cur=head
    if head is None:
        return head
    if x is 1:
        head=cur.next
        head.prev=None
        return 
    while(count<x and cur is not None):
        count+=1
        cur=cur.next
    if(cur.next is None):
        cur.prev.next=None
    else:
        cur.prev.next=cur.next
        cur.next.prev=cur.prev
        
            
            
        
            