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


def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    ans=[k,0]
    def inOrder(root):
        if root==None: return None
        inOrder(root.left)
        ans[1]+=1
        if ans[1]==ans[0]: ans.append(root.val)                       
        inOrder(root.right)
    inOrder(root)
    return ans[2]
                        

root=buildTree([3,1,4,None,2])
print(kthSmallest(root,1))

root=buildTree([5,3,6,2,4,None,None,1])
print(kthSmallest(root,3))

