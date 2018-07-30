{
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()
if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        llist.head = pairWiseSwap(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa

}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""  Pairwise swap the elements in a linked list.
  The input list will have at least one element
  Return reference to head of rotated linked list
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def pairWiseSwap(head):
    # code here
    curr = head
    if curr is None:
        return curr
    else:
        t = head
        
        #curr = curr.next
        while curr is not None and curr.next is not None:
            temp = curr.data
            curr.data =curr.next.data
            curr.next.data = temp
            curr = curr.next.next
        return t
            