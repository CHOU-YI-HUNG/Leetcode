# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def PreOrder(root):
    if root!=None:
        print(root.val)
        PreOrder(root.left)        
        PreOrder(root.right)

def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """        
    def traversal(l1,r1,l2,r2):                                        
        if l1>r1: return None    
        root=TreeNode(preorder[l1])        
        j=0
        while(preorder[l1]!=inorder[l2+j]):j+=1                                            
        root.left=traversal(l1+1,l1+j,l2,l2+j-1) 
        root.right=traversal(l1+j+1,r1,l2+j+1,r2) 
        return root                                    
    return traversal(0,len(preorder)-1,0,len(preorder)-1)



# head=buildTree([1,2],[1,2])
head=buildTree([3,9,20,15,7],[9,3,15,20,7])
PreOrder(head)
