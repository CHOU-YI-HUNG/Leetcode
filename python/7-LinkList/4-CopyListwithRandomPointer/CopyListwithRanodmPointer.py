class Node(object):
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
        
def createListNode(list):    
    val,_=list[len(list)-1]
    table=[]
    a=Node(val)
    table.append(a)
    for i in range(len(list)-2,-1,-1):                
        val,_=list[i]
        b=Node(val,a)        
        table.append(b)
        a=b
    
    table.reverse()
    sRan=a
    for i in range(len(list)):
        _,random=list[i]
        sRan.random=table[random] if random!=None else None
        sRan=sRan.next                        
    return a

def copyRanodmList(head:Node):
    
    if head==None: return None
    # Record head and new head, their correspondence to the index
    oldTable={}
    newtable={}
    index=0            
    shead=head# Record start head
    oldTable[head]=index    
    start=pre=cur=Node(head.val)
    newtable[index]=cur    
    index+=1
    head=head.next    
    while head!=None:        
        oldTable[head]=index
        cur=Node(head.val)
        newtable[index]=cur
        pre.next=cur
        
        pre=cur
        index+=1
        head=head.next    
    
    cur=start                
    while shead!=None:
        print(oldTable[shead.random] if shead.random!=None else None)
        cur.random=newtable[oldTable[shead.random]] if shead.random!=None else None        
        cur=cur.next
        shead=shead.next
    return start

head=createListNode([[7,None],[13,0],[11,4],[10,2],[1,0]])
start=copyRanodmList(head)
Exampe=[]
while start!=None:
    Exampe.append([start.val,start.random.val if start.random!=None else None]) 
    start=start.next
print(Exampe)    


