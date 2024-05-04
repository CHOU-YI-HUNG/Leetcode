# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int        
    """        
    if root==None:return 0    
    result=max(1+maxDepth(root.right),1+maxDepth(root.left))    
    return result
    

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
def InOrder(root):
    if root!=None:
        InOrder(root.left)
        print(root.val)
        InOrder(root.right)
def PreOrder(root):
    if root!=None:
        print(root.val)
        PreOrder(root.left)        
        PreOrder(root.right)
def PostOrder(root):
    if root!=None:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.val)
        

input=[3,9,20,None,None,15,7]
input=[1,None,2]
root=BuildTree(input)
print(maxDepth(root))


