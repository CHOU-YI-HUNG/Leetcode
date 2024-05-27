
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
def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # get to the bottom of the tree and count the number of nodes at the last level for N
    #2^{h}-1-(h-N)    
    if root==None: return 0
    h=0
    queue=[root]
    
    while len(queue)==pow(2,h):
        queueSize=len(queue)        
        for i in range(queueSize):  
            root=queue.pop(0)                                  
            if root.left!=None:queue.append(root.left)                                            
            if root.right!=None:queue.append(root.right)
        h+=1
    return (2<<h)-1-((2<<h-1)-len(queue))


root=BuildTree([1,2,3,4])
print(countNodes(root))
root=BuildTree([1,2,3,4,5])
print(countNodes(root))

root=BuildTree([1,2,3,4,5,6])
print(countNodes(root))








# if root==None: return 0    
#     neighbors=[]
#     count=1
#     while True:
#         if root.left==None and root.right==None:            
#             if neighbors and neighbors[-1]!=None: 
#                 count-=1
#                 root=neighbors.pop()
#             else: break
            
#         if root.right!=None:
#             count=2*count+1
#             neighbors.append(root.left)
#             root=root.right
#         else:
#             count=2*count
#             neighbors.append(root.right)
#             root=root.left


