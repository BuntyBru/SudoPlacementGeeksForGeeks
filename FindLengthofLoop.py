class Node:
	def __init__(self,data):
		self.data = data
		self.next= None
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		t = Node(new_data)
		t.data = new_data
		t.next = self.head
		self.head = t

	def printList(self):
		temp = self.head

		while temp:
			print(temp.data,end=" ")
			temp = temp.next

	def DetectLoop(self):
		s =set()
		count = 0
		temp = self.head
		while temp:
			if temp in s:
				return count
			s.add(temp)
			temp = temp.next
			count= count+1
		return 0

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
  
llist.head.next.next = llist.head;
 
t = llist.DetectLoop()
if t >0 :
    print (t)
else:
    print ("No Loop ")

