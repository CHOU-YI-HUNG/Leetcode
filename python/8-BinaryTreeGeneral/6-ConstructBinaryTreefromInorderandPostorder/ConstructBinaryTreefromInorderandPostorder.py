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

def InOrder(root):
    if root!=None:
        InOrder(root.left)
        print(root.val)
        InOrder(root.right)

def buildTree(inorder,postorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """    
    if not postorder: return None    
    lastIndex=len(postorder)-1
    root=TreeNode(postorder[lastIndex])     
    j=0    
    while(postorder[lastIndex]!=inorder[j]):j+=1    
    root.left=buildTree(inorder[0:j],postorder[0:j])     
    root.right=buildTree(inorder[j+1:lastIndex+1],postorder[j:lastIndex])                                 
    return root




head=buildTree([9,3,15,20,7],[9,15,7,20,3])
PreOrder(head)
