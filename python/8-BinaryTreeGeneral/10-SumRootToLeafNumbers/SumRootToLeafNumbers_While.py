# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


def sumNumbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """            
    if root==None: return None
    TotoalSum=0    
    path=0    
    pathStack=[]
    stack=[root]    
    while stack:                                        
        path=path*10+root.val
        if root.right!=None:
            pathStack.append(path)
            stack.append(root.right)        
        if root.left!=None:
            pathStack.append(path)
            stack.append(root.left)                                
                                                        
        if root.left==None and root.right==None:                                         
            TotoalSum+=path
        
        root=stack.pop()      
        path=pathStack.pop() if pathStack else 0        
    return TotoalSum
        

root=BuildTree([1,2,3])
print(sumNumbers(root))

root=BuildTree([4,9,0,5,1])
print(sumNumbers(root))






