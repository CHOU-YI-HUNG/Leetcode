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
    if not root:return []            
    s = [root]        
    ChildLevel=[]
    ParentsLevel=[]
    ans=[float]
    while s:
        cur = s[-1]
        if not cur.left and not cur.right:
            s.pop()
            # PostOrder Section     
            # if  not ChildLevel:
            #     ChildLevel.append(cur)            
            # else:
            #     if not ParentsLevel and cur.left==ParentsLevel[-1] or cur.right==ParentsLevel[-1]: 
            #         sum=0
            #         for e in ChildLevel:sum=sum+e                        
            #         ans.append(sum/len(ChildLevel))
                    
            #         sum=0
            #         for e in ParentsLevel:sum=sum+e                               
            #         ans.append(sum/len(ParentsLevel))
                    
            #         ChildLevel=[]
            #         ParentsLevel=[]
                               
            #     elif cur.left==ChildLevel[-1] or cur.right==ChildLevel[-1]:
            #         ParentsLevel.append(cur)
            #     else:
            #         ChildLevel.append(cur)
            
            print(cur.val)
            # End

        if cur.right:
            s.append(cur.right)
            cur.right = None
        
        if cur.left:
            s.append(cur.left)
            cur.left = None            
    
    if ChildLevel:
        sum=0
        for e in ChildLevel:sum=sum+e                        
        ans.append(sum/len(ChildLevel))
    if ParentsLevel:
        sum=0
        for e in ParentsLevel:sum=sum+e                               
        ans.append(sum/len(ParentsLevel))
    return ans

root=buildTree([3,9,20,None,None,15,7])
print(averageOfLevels(root))



