class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    stackRecord=[]
    stack=[root]
    while stack:                
        node=stack.pop()
        #       
        if not stackRecord:
            stackRecord.append(node)
        elif stackRecord[-1].left==node:
            stackRecord.append(node)
        else:
            stackRecord.pop()                        
        #
        print(node.val)
        print(stackRecord)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        
def traversal(root):
    stackRecord=[]
    stack=[root]
    while stack:                
        node=stack.pop()
        #       
        if not stackRecord:
            stackRecord.append(node)
        elif stackRecord[-1].left==node:
            stackRecord.append(node)
        else:
            stackRecord.pop()       
            stackRecord.append(node)                 
        #

        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
root=BuildTree([1,2,3,4,5,6])
traversal(root)

def traversal(root):
    stack=[root]
    while stack:                
        node=stack.pop()
        print(node.val)        
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
