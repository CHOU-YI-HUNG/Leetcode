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
			curr.left = TreeNode(nums[i])
			q.append(curr.left)
			i += 1
		if i < len(nums):
			curr.right = TreeNode(nums[i])
			q.append(curr.right)
			i += 1
	return root

def printTree(root):
    if not root: return
    print(root.val, end=" ")
    printTree(root.left)	
    printTree(root.right)

nums = [1, 2, 3, None, 5, None, 4]
root = buildTree(nums)
printTree(root)
















