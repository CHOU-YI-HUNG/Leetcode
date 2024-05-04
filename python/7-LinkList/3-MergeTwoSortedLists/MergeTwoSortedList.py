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
def mergeTwoLists(list1,list2):
    #insert sort
    # list1 insert list2    
    if list1==None or list2==None:        
        return list1 if list1!=None else list2
         
    if list1.val<=list2.val:
        hand=list1
        cards=list2
    else:
        hand=list2
        cards=list1
    
    pre=start=hand         
    while cards!=None and hand!=None: 
        if cards.val>=hand.val:
            pre=hand
            hand=hand.next
        else:
            pre.next=cards
            pre=pre.next
            temp=cards.next
            cards.next=hand
            cards=temp                                    
    if cards!=None:
        pre.next=cards                            
    return start

l1=createListNode([1,2,4])
l2=createListNode([1,3,4])
start=mergeTwoLists(l1,l2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)    

l1=createListNode([1])
l2=createListNode([2])
start=mergeTwoLists(l1,l2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)    


l1=createListNode([-9,3])
l2=createListNode([5,7])
start=mergeTwoLists(l1,l2)
Exampe=[]
while start!=None:
    Exampe.append(start.val)    
    start=start.next
print(Exampe)  