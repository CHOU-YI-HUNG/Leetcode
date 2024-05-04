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


def rotateRight(head,k):
    #先做一次，如果K<Lenght of Linked List 
    if head==None: return None
    if k==0:return head
    start=pre=cur=head
    count=1
    while cur.next!=None and count<=k:
        count+=1
        cur=cur.next        
    if cur.next!=None:
        while cur.next!=None:
            pre=pre.next       #3
            cur=cur.next  #5
        cur.next=head
        start=pre.next #4
        pre.next=None                
    else:#如果沒有做完，先把k取餘數，在重複上次的
        k%=count
        start=pre=cur=head
        count=1
        while cur.next!=None and count<=k:
            count+=1
            cur=cur.next        
            
        while cur.next!=None:
            pre=pre.next  #3
            cur=cur.next  #5
        cur.next=head
        start=pre.next #4
        pre.next=None                                            
    return start


head=createListNode([1,2,3,4,5])
start=rotateRight(head,7)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)

head=createListNode([0,1,2])
start=rotateRight(head,4)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)