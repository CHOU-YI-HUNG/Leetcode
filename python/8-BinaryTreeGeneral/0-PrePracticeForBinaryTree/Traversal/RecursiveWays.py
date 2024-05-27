def InOrder(root):
    if root!=None:
        InOrder(root.left)
        print(root.val)
        InOrder(root.right)
        
def PreOrder(root):
    if root!=None:
        print(root.val)
        PreOrder(root.left)        
        PreOrder(root.right)
        
def PostOrder(root):
    if root!=None:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.val)        