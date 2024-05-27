
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
def BuildTree(input):
    root=cur=Node(input[0])
    TreeList=[root]    
    i=1
    while i<len(input):
        cur=TreeList[((i+1)//2)-1]
        newNode=Node(input[i]) if input[i]!=None else None
        TreeList.append(newNode)
        if (i+1)%2==0:            
            cur.left=newNode            
        else:
            cur.right=newNode
        i+=1
    return root


def connect(root):
    """
    :type root: Node
    :rtype: Node
    """                                                                                                                                           
    if root==None: return None        
    queue=[root]    
    while queue:
        n=len(queue)                
        for i in range(n):
            node=queue.pop(0)                    
            node.next=queue[0] if i<(n-1) else None
            if node.left!=None: queue.append(node.left)
            if node.right!=None: queue.append(node.right)                                            
    return root

def PrintOrder(root):
    if root==None: return None
    next=root
    while next!=None:
        print(next.val)
        next=next.next   
    print("##")         
    PrintOrder(root.left)

root=BuildTree([1,2,3,4,5,None,7])
root=connect(root)
PrintOrder(root)

# root=BuildTree([0,2,4,1,None,3,-1,5,1,None,6,None,8])
# connect(root)
# PrintOrder(root)

