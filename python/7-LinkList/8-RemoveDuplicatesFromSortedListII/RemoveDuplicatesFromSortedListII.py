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
def deleteDuplicates(head):    
    start=pre=cur=None    
    while head!=None:
        if head.val!=(head.next.val if head.next!=None else None) and head.val!=(pre.val if pre!=None else None):
            if start==None:
                cur=start=head
            else:
                cur.next=head
                cur=cur.next
        
        pre=head
        head=head.next 
                             
    if cur!=None:cur.next=None
    return start
        
        
    


head=createListNode([1,2,3,3,4,4,5])
start=deleteDuplicates(head)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([1,1,1,2,3])
start=deleteDuplicates(head)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)


head=createListNode([0,1,2,2,3,4])
start=deleteDuplicates(head)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)