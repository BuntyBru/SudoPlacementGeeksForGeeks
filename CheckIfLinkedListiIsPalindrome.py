
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
# your task is to complete this function
# function should return true/false or 1/0
def isPalindrome(head):
    # Code here
    curr = head
    if head is None:
        return True
    if curr.next is None:
        return True
    else:
        arr = []
        
        while curr:
            arr.append(curr.data)
            curr=curr.next
        temp = head
        count=0
        i=0
        #print(arr)
        arr.reverse()
        while temp:
            if temp.data == arr[i]:
                count=count+1
                i=i+1
            temp=temp.next
        #print(count)
        if count == len(arr):
            return True
        else:
            return False
        
            
        