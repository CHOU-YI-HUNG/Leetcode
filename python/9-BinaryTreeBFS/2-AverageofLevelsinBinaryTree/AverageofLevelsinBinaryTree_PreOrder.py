class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def buildTree(nums):
	if not nums:
		return None
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

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    ansTemp=[]
    def PreOrder(node,layer):
        if node!=None:
            if layer>len(ansTemp)-1:ansTemp.append((node.val,1))
            else:
                val,count=ansTemp[layer]
                val+=node.val
                count+=1
                ansTemp[layer]=(val,count)
            PreOrder(node.left,layer+1)        
            PreOrder(node.right,layer+1)
    PreOrder(root,0)
    i=0
    for val, count in ansTemp:
        ansTemp[i]=val/count
        i+=1
    return ansTemp
    
root=buildTree([3,9,20,None,None,15,7])
print(averageOfLevels(root))



