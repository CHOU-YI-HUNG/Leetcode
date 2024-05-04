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

def LeftandRightNode(L,R):
    if L==R: return True    
    if L==None or R==None or L.val!=R.val: return False    
    return LeftandRightNode(L.left,R.right) and LeftandRightNode(L.right,R.left)

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return LeftandRightNode(root.left,root.right)    
root=BuildTree([1,2,2,3,4,4,3])

# root=BuildTree([1,2,2,None,3,None,3])
print(isSymmetric(root))



