class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BuildTree(input):
    if not input: return None
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

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(nums):
	if not nums:
		return None
	root = TreeNode(nums[0])
	q = [root]
	i = 1
	while i < len(nums):
		curr = q.pop(0)
		if i < len(nums):
			curr.left = TreeNode(nums[i])
			q.append(curr.left)
			i += 1
		if i < len(nums):
			curr.right = TreeNode(nums[i])
			q.append(curr.right)
			i += 1
	return root
def PreOrder(root):
    if root!=None:
        print(root.val)
        PreOrder(root.left)        
        PreOrder(root.right)

def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root==None: return None
    queue=[root]
    ans=[]
    while queue:
        ans.append(queue[-1].val)
        n=len(queue)
        for i in range(n):                        
            node=queue.pop(0)               
            if node.left!=None: queue.append(node.left)
            if node.right!=None: queue.append(node.right)
    return ans
    
root=BuildTree([1,2,3,None,5,None,4])
print(rightSideView(root))

root=BuildTree([1,None,3])
print(rightSideView(root))

root=BuildTree([])
print(rightSideView(root))
