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
stack=[]
def flatten(root):                
    if root==None: return None
    if root.right!=None: stack.append(root.right)
    if root.left!=None: stack.append(root.left)
    root.right=flatten(stack.pop()) if stack else None
    root.left=None                    
    return root

def PreOrder(root):
    if root!=None:
        print(root.val)
        PreOrder(root.left)        
        PreOrder(root.right)

root=BuildTree([1,2,5,3,4,None,6])
root=flatten(root)
PreOrder(root)