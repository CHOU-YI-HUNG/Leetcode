
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

def reverseBetween(head, left, right):
    if  head==None or head.next==None or right-left==0: return head
    start=head
    position=1
    while position<left-1:        
        head=head.next
        position+=1        
        
    if left>1:        
        cur=pre=head.next # head=1, head.next=2
        nextone=cur.next
        for i in range(right-left):                
            cur=nextone        
            nextone=cur.next                             
            cur.next=pre
            pre=cur
        (head.next).next=nextone # 2->5
        head.next=cur #1->4                        
    else:        
        cur=pre=head# head=3        
        nextone=cur.next # head=5
        for i in range(right-left):                
            cur=nextone        
            nextone=cur.next                             
            cur.next=pre
            pre=cur
        head.next=nextone
        start=cur     
    return start


head=createListNode([1,2,3,4,5])
start=reverseBetween(head,2,4)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)   


head=createListNode([3,5])
start=reverseBetween(head,1,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)   
