def delNode(head, k):
    prev=head
    cur=head
    count=1
    if head is None:
        return None
    elif k is 1:
        head=head.next
        return head
        
    else:
        while(cur is not None and count<k):
            prev=cur
            cur=cur.next
            count+=1
        prev.next=cur.next
        
    return head