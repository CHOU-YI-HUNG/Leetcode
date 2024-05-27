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
    def Rec(root,path):                
        if root==None: return None  
        path=(path*10+root.val)
        Rec(root.left,path)
        Rec(root.right,path)                                                  
        if root.left==None and root.right==None: 
            global TotalSum
            TotalSum+=path                        
    Rec(root,0) 
    return TotalSum

root=BuildTree([1,-2,-3,1,3,None,-1])
TotalSum=0
print(sumNumbers(root))        

root=BuildTree([1,2,3])
TotalSum=0
print(sumNumbers(root))

root=BuildTree([4,9,0,5,1])
TotalSum=0
print(sumNumbers(root))






