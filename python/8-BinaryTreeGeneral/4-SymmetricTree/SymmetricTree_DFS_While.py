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

   

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    stackLeft=[root]
    stackRight=[root]
    LeftNode=root.left    
    RightNode=root.right
    
    # if the list is empty,  then it return False.
    while stackLeft or stackRight:
        if LeftNode==RightNode: 
            LeftNode=stackLeft.pop()
            RightNode=stackRight.pop()    
            continue
        if LeftNode==None or RightNode==None: return False
        
        if LeftNode.val!=RightNode.val:return False
            
        stackLeft.append(LeftNode.left)
        stackLeft.append(LeftNode.right)
        
        stackRight.append(RightNode.right)
        stackRight.append(RightNode.left)
        
        LeftNode=stackLeft.pop()
        RightNode=stackRight.pop()
                                                        
    return True
    

root=BuildTree([1,2,2,3,4,4,3])

root=BuildTree([1,2,2,None,3,None,3])
print(isSymmetric(root))



