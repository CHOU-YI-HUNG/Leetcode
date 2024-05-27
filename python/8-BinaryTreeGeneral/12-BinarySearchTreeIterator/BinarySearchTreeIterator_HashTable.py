# Definition for a binary tree node.
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

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.curIndex=0        
        self.count=0
        self.hashTable={}
        self.InorderPath(root)        
        
    def InorderPath(self,root):
        if root==None: return None        
        self.InorderPath(root.left)        
        self.hashTable[self.count]=root
        self.count+=1
        self.InorderPath(root.right)
        
            
    def next(self):
        """
        :rtype: int
        """
        self.curIndex+=1        
        return self.hashTable[self.curIndex-1].val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curIndex>=self.count:return False                    
        return True
    
root=BuildTree([2,1])
obj=BSTIterator(root)
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())

root=BuildTree([1,None,2])
obj=BSTIterator(root)
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
        
root=BuildTree([1])
obj=BSTIterator(root)
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())


# root=BuildTree([7,3,15,None,None,9,20])
# obj=BSTIterator(root)
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next()) #20
# print(obj.hasNext())

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



