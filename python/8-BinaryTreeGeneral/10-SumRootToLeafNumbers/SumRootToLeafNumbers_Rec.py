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
        global TotalSum
        if root==None: return None
        if root.left==None and root.right==None: 
            path+=str(root.val)            
            TotalSum+=int(path)
            return None        
        path+=str(root.val)
        Rec(root.left,path)
        Rec(root.right,path)
    Rec(root,"")        
    return TotalSum
        

root=BuildTree([1,2,3])
TotalSum=0
print(sumNumbers(root))

root=BuildTree([4,9,0,5,1])
TotalSum=0
print(sumNumbers(root))






