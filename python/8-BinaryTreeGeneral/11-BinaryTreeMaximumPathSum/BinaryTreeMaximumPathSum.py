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



def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    def Rec(root,Sum,max_value,parent,localMax):
        if root==None: return None,-1001,localMax
        
        # if root.right==None and root.left==None: return root.val                
        cur=root
        a=root.val
        LN,b,localMax=Rec(root.left,Sum,max_value,root,localMax)                
        RN,c,localMax=Rec(root.right,Sum,max_value,root,localMax)
        if root.left!=LN and root.right!=RN: 
            if a>max(b,c):
                Sum=a
            else:
                if b>c:
                    cur=LN
                    Sum=b                
                else:
                    cur=RN
                    Sum=c                                                                                       
        elif root.left!=LN and root.right==RN: 
            if max(a,a+c)>max(b,c):
                Sum=max(a,a+c)            
            else:
                if b>c:
                    cur=LN
                    Sum=b                
                else:
                    cur=RN
                    Sum=c                                       
        elif root.left==LN and root.right!=RN: 
            if max(a,a+b)>max(b,c):                
                Sum=max(a,a+b)                            
            else:
                if b>c:
                    cur=LN
                    Sum=b                
                else:
                    cur=RN
                    Sum=c 
        else:# root.left==LN root.right==RN, and and (max(a+b+parent.val,a+c+parent.val)>a+b+c): 
            if a+b+c>max(a,b,c,a+b,a+c):
                localMax=max(a+b+c,localMax)
            if max(a,a+b,a+c,a+b+c)>max(b,c):                
                    if parent==None:
                        Sum=max(a,a+b,a+c,a+b+c)            
                    else:    
                        Sum=max(a,a+b,a+c)            
            else:
                if b>c:
                    cur=LN
                    Sum=b                
                else:
                    cur=RN
                    Sum=c            
        max_value=max(Sum,max_value)    
        return cur,max_value,localMax                                                                        
    _,result,localMax=Rec(root,0,-1001,None,-1001)
    return  max(result,localMax)

root=BuildTree([8,9,-6,None,None,5,9])  
print(maxPathSum(root)) #20

root=BuildTree([5,4,8,11,None,13,4,7,2])  
print(maxPathSum(root)) #48


root=BuildTree([-10,9,20,None,None,15,7])  
print(maxPathSum(root)) #42

root=BuildTree([1,2,3])  
print(maxPathSum(root))#6
    
root=BuildTree([1,-2,-3,1,3,-2,None,-1])
print(maxPathSum(root))#3

root=BuildTree([1,2])
print(maxPathSum(root)) #3

root=BuildTree([-2,1])
print(maxPathSum(root)) #1

root=BuildTree([-3])
print(maxPathSum(root)) #-3

# def maxPathSum(root):
#     """
#     :type root: TreeNode
#     :rtype: int
#     """
#     def Rec(root,Max_value,Sum,parent):
#         if root==None: return None, None                
#         if root.val>root.val+Sum:
#             cur=root
#             Sum=root.val
#         else:
#             cur=parent
#             Sum=root.val
#         #Max_value=max(Max_value,Sum)
        
#         LR,LS=Rec(root.left,Max_value,Sum,root)                    
#         RR,RS=Rec(root.right,Max_value,Sum,root)
        
#         # Leaf node
#         if LR==None and RR==None: return cur,Sum
#         # ond node
#         if LR==None:
#             return RR,max(RS+Sum,RS)
#         if RR==None:
#             return LR,max(LS+Sum,LS)
#         # Complete node
#         if LR==RR: return parent,(LS+RS+root.val)        
#         if LS>RS:
#             return LR,LS
#         else:                                     
#             return RR,RS
#     _,sumation=Rec(root,-1000,0,None)
#     return sumation
