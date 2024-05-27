class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BuildTree(input):
    root=cur=TreeNode(input[0])
    TreeList=[root]    
    i=1
    while i<len(input):
        cur=TreeList[((i+1)//2)-1]
        newNode=TreeNode(input[i]) if input[i]!=None else None
        TreeList.append(newNode)
        if (i+1)%2==0:            
            cur.left=newNode            
        else:
            cur.right=newNode
        i+=1
    return root

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    global pindex
    global qindex
    global rtypeRoot
    # Traverse the root to find the index of p and q by PreOrder
    def Traversal1(root,count,p,q):
        global pindex
        global qindex
        if root==None: return None                        
        if qindex!=-1 and pindex!=-1: return                 
        if q==root:qindex=count
        if p==root:pindex=count
            
        Traversal1(root.left,2*count,p,q)    
        Traversal1(root.right,2*count+1,p,q)        
    def Traversal(root,count,index):        
        global rtypeRoot
        if root==None: return 0                        
        if count==index:rtypeRoot=root                                     
        Traversal(root.left,2*count,index)
        Traversal(root.right,2*count+1,index)
        
        
    Traversal1(root,1,p,q)        
    while pindex//2!=qindex//2:
        if pindex>qindex:
            pindex=pindex//2
        else:
            qindex=qindex//2    
    Traversal(root,1,pindex//2)
                
    return rtypeRoot
pindex=-1
qindex=-1
rtypeRoot=TreeNode
root=BuildTree([3,5,1,6,2,0,8])



def Traversal(root):
    # Traverse the root to find the index of p and q by PreOrder
    index=1
    StackRoot=[root]
    StackCount=[index]    
    while StackRoot:                               
        
        root=StackRoot.pop(0)
        index=StackCount.pop(0)
        
        if root!=None:                                    
            if root.left!=None:
                StackRoot.append(root.left)
                StackCount.append(2*index) 
            StackRoot.append(root)
            StackCount.append(index)
            if root.right!=None:
                StackRoot.append(root.right)
                StackCount.append(2*index+1)
            
                                                       
            root=root.left
            index=2*index            
            
        else:            
            index=StackCount.pop(0)    
            root=StackRoot.pop(0)        
            root=root.right
            # index=2*index+1                         




