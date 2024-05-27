class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(nums):
	if not nums:return None		
	root = TreeNode(nums[0])
	q = [root]
	i = 1
	while i < len(nums):
		curr = q.pop(0)
		if i < len(nums):            
			curr.left = TreeNode(nums[i]) if nums[i]!=None else None
			q.append(curr.left)
			i += 1
		if i < len(nums):
			curr.right = TreeNode(nums[i]) if nums[i]!=None else None
			q.append(curr.right)
			i += 1
	return root

def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    ans=[None]
    def inOrder(root):
        if root==None: return True
        L=inOrder(root.left)        
        if ans[0]==None: ans[0]=root.val
        else:
            if ans[0]>root.val:return False                 
            ans[0]=root.val
        R=inOrder(root.right)        
        return L and R        
    return inOrder(root)


root=buildTree([2,1,3])
print(isValidBST(root))

root=buildTree([5,1,4,None,None,3,6])
print(isValidBST(root))
