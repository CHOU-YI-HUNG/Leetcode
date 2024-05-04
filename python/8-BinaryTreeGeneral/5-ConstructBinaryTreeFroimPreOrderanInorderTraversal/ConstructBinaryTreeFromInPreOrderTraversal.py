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

def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """    
    if not preorder: return None
    root=TreeNode(preorder[0]) 
    j=0    
    while(preorder[0]!=inorder[j]):j+=1    
    root.left=buildTree(preorder[1:j+1],inorder[0:j]) 
    root.right=buildTree(preorder[j+1:],inorder[j+1:])                                 
    return root



# head=buildTree([1,2],[1,2])
head=buildTree([3,9,20,15,7],[9,3,15,20,7])
PreOrder(head)
