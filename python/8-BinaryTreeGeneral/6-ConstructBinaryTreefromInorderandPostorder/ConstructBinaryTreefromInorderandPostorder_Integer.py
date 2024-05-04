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
    def traversal(l1,r1,l2,r2):
        if l1>r1: return None                    
        root=TreeNode(postorder[r2])     
        j=0    
        while(postorder[r2]!=inorder[l1+j]):j+=1                 
        root.left=traversal(l1,l1+j-1,l2,l2+j-1)
        root.right=traversal(l1+j+1,r1,l2+j,r2-1)
        return root
    return traversal(0,len(inorder)-1,0,len(postorder)-1)




head=buildTree([9,3,15,20,7],[9,15,7,20,3])
PreOrder(head)
