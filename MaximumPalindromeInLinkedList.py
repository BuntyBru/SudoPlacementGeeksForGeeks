{
# Node Class
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        print(maxPalindrome(list1.head))
# Contributed By: Harshit Sidhwa

}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function should return an integer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
def maxPalindrome(head):
    # Code here
    lst = []
    while(head!=None):
        lst.append(head.data)
        head = head.next
    #print(lst)
    val = 1
    for i in range(len(lst)):
        for j in range(i):
            #print("lst[j:i+1] ",lst[j:i+1])
            #print("lst[j:i+1][::-1] ",lst[j:i+1][::-1])
            
            if(lst[j:i+1] == lst[j:i+1][::-1] and len(lst[j:i+1])>val):
                #print("Inside  ")
                val = len(lst[j:i+1])
                #print("val ",val)
                #print("----------------------")
                
    return val