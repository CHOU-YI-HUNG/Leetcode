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

def hasPathSum(root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: bool
    """
    targetSum=targetSum
    def Rec(root,CurSum):
        if root==None: return False    
        CurSum+=root.val
        if root.left==None and root.right==None and CurSum==targetSum: return True                  
        return Rec(root.left,CurSum) or Rec(root.right,CurSum)
    return Rec(root,0)
                
    
    
    
root=BuildTree([5,4,8,11,None,13,4,7,2])
print(hasPathSum(root,22))

root=BuildTree([1,2,3])
print(hasPathSum(root,5))


print(hasPathSum(None,0))
