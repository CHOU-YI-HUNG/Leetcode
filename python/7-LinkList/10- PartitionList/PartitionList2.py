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

def partition(head,x):
    if head==None: return None
    if head.next==None: return head
    c=d=None
    a=b=cur=head
    while cur!=None and cur.val<x:        
        b=cur
        cur=cur.next    
    
    #second part
    c=d=cur
    if a==c: return c
    if cur==None: return a
    
    if cur!=None: #後面有東西要分        
        while cur.next!=None:           
            cur=cur.next
            if cur.val<x:
                b.next=cur
                b=b.next
            else:
                d.next=cur
                d=d.next                                  
        
    d.next=None        
    b.next=c 
    return a




head=createListNode([1,4,3,2,5,2])
start=partition(head,3)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([2,1])
start=partition(head,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([4,3,2,5,2])
start=partition(head,3)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)


head=createListNode([1,4,3,0,5,2])
start=partition(head,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([1,4,3,0,2,5,2])
start=partition(head,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)


head=createListNode([1,1])
start=partition(head,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([1,1])
start=partition(head,0)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)