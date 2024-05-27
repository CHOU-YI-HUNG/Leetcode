# Definition for a binary tree node.
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

def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    ans=[]
    def PreOrder(root,level):
        if root!=None:
            if level>len(ans)-1:ans.append([root.val])
            else:
                if (level%2)==0:ans[level].append(root.val)                    
                else:ans[level].insert(0,root.val)                    
            PreOrder(root.left,level+1)
            PreOrder(root.right,level+1)                                    
    PreOrder(root,0)
    return ans


root=buildTree([3,9,20,None,None,15,7])
print(zigzagLevelOrder(root))


