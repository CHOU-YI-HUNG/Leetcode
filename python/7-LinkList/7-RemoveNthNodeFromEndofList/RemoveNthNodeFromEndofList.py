class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def createListNode(list):    
    a=ListNode(list[len(list)-1])
    for i in range(len(list)-2,-1,-1):                
        b=ListNode(list[i],a)        
        a=b
    return a


def removeNthFromEnd(head, n):
    if head.next==None: return None
    if n>1:
        p1=p2=head
        pre=None
        for i in range(n-1):        
            p2=p2.next                            
        while p2.next!=None:
            pre=p1
            p1=p1.next
            p2=p2.next

        if pre!=None:        
            pre.next=p1.next
        else:
            head=p1.next
        del p1
    else:
        p1=head
        while p1.next.next!=None:
            p1=p1.next
        p1.next=None        
    return head    



head=createListNode([1,2,3,4,5])
start=removeNthFromEnd(head,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)



head=createListNode([1])
start=removeNthFromEnd(head,1)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)


head=createListNode([1,2])
start=removeNthFromEnd(head,1)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)


head=createListNode([1,2,3,4,5,6,7,8,9,10])
start=removeNthFromEnd(head,7)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)
