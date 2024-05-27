import math
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
    if root==None: return None        
    queue=[root]    
    ans=[]
    while queue:
        n=len(queue)                
        summation=0
        for i in range(n):
            # 每一層node都會經過這裡            
            node=queue.pop(0)       
            summation+=node.val                         			                       
            if node.left!=None: queue.append(node.left)
            if node.right!=None: queue.append(node.right)
        # 到下一層的node
        ans.append(summation/n)        
    return ans

root=buildTree([3,9,20,15,7])
print(averageOfLevels(root))
print(math.log(pow(10,4),2))
