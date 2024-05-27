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

def InOrder(root):
    stack = []     
    while stack or root!=None:
        while root != None:
            stack.append(root)
            root = root.left    
        root = stack.pop()
        #InOrder Section
        print(root.val)
        #End
        root = root.right
        
def PreOrder(root):
  stack=[root]
  while stack:                
    root=stack.pop()
    #PreOrder Section
    print(root.val)
    #End          
    if root.right: stack.append(root.right)
    if root.left: stack.append(root.left)
        
        
    
def PostOrder(root) :
    if not root:return []            
    s = [root]        
    while s:
        cur = s[-1]
        if not cur.left and not cur.right:
            s.pop()
            # PostOrder Section            
            print(cur.val)
            # End

        if cur.right:
            s.append(cur.right)
            cur.right = None
        
        if cur.left:
            s.append(cur.left)
            cur.left = None            

        
        
root=BuildTree([1,2,3,4,5,6,7])        
# print("PreOrder")
# PreOrder(root)
# print("InOrder")
# InOrder(root)
print("PostOrder")
postorderTraversal(root)

