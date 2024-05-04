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

def PreOrder(root):
    if root!=None:
        print(root.val)
        PreOrder(root.left)        
        PreOrder(root.right)

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root==None: return None        
    root.left,root.right=root.right,root.left    
    invertTree(root.right)
    invertTree(root.left)    
    return root
    
    
    
        
root=BuildTree([4,2,7,1,3,6,9])
root=invertTree(root)
PreOrder(root)
