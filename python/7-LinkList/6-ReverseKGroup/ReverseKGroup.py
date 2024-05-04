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


def reverseKGroup(head, k):
    # Length of list < k
    if head==None: return head
    pre=cur=head #1
    count=1    
    nextone=head.next #2    
    while nextone!=None and count<k:
        cur=nextone #2
        nextone=cur.next #3
        cur.next=pre #2->1
        pre=cur #2        
        count+=1
    
    if nextone==None and count<k: # terminal condition                
        if count>1:
            preOne=None
            pre=cur.next            
            for i in range(count-1):
                cur.next=preOne            
                preOne=cur
                cur=pre
                pre=pre.next                      
        return head
    else:             
        head.next=reverseKGroup(nextone,k)
        return cur
        

head=createListNode([1,2,3,4,5])
start=reverseKGroup(head,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([1,2,3,4,5])
start=reverseKGroup(head,3)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([1,2])
start=reverseKGroup(head,2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

