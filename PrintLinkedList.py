def printlist(node):
    #code here
    if node is None:
        return 
    if node is not None:
        while(node is not None):
            print(node.data,end=' ')
            node=node.next