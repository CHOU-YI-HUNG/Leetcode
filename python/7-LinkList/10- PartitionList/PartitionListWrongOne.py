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
    
    remain=pre=None
    cur=head    
    
    while cur.val<x:
        pre=cur
        cur=cur.next
    remain=pre
    insertPoint=cur
    while cur!=None:
        if cur.val<x:
            if remain!=None:                                    
                pre.next=cur.next                    
                remain.next=cur
                remain=cur
            else:
                pre.next=cur.next
                head=remain=cur                                                     
    
        # if cur.next!=None:
        #     if  not(cur.val<x and cur.next.val<x):pre=cur                        
        # if cur.next==None:pre=cur        
        pre=cur    
        cur=cur.next
        
    pre.next=insertPoint
    return head




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