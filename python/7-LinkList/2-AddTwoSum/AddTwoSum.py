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

def addTwoNumbers(l1,l2):        
    # initialized    
    val=(l1.val+l2.val)%10        
    pre=cur=start=ListNode(val)
    carry=(l1.val+l2.val)//10
    l1=l1.next
    l2=l2.next
    # start 1
    while l1!=None and l2!=None:
        total=l1.val+l2.val+carry
        val=(total)%10        
        carry=(total)//10        
        cur=ListNode(val)        
        pre.next=cur                        
        pre=cur
        l1=l1.next
        l2=l2.next
    
    # when l1 isn't same size compare to l2
    node= l1 if l1!=None else l2
    while node!=None:
        total=node.val+carry
        val=total%10
        carry=total//10
        cur=ListNode(val)
        pre.next=cur                        
        pre=cur
        node=node.next
        
    if carry!=0:
        cur=ListNode(carry)
        pre.next=cur             
    return start
    

l1=createListNode([2,4,3])
l2=createListNode([5,6,4])
start=addTwoNumbers(l1,l2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)    


l1=createListNode([0])
l2=createListNode([0])
start=addTwoNumbers(l1,l2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)    

l1=createListNode([9,9,9,9,9,9,9])
l2=createListNode([9,9,9,9])
start=addTwoNumbers(l1,l2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)    



