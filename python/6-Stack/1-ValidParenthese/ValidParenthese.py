def isValid(s):    
    Chekclist={"(":(0,1),")":(1,1),"[":(0,2),"]":(1,2),"{":(0,3),"}":(1,3)}
    result=[]
    for e in s:
        InorOut,category=Chekclist[e]
        if InorOut==0: # input
            result.append(category)
        else: # output  
            if len(result)==0: #input doesn't happen
                return False  
            if result.pop()!=category:
                return False
    if len(result): # has input but no output
        return False
    return True



s="("
print(isValid(s))

s="()[]{}"
print(isValid(s))

s="(]"
print(isValid(s))

s="([)]"
print(isValid(s))



# def isValid(s):
#     smallCheck=0
#     middleCheck=0
#     lagerCheck=0
#     for e in s:        
#         if e=="(":
#             smallCheck+=1
#         elif e=="[":
#             middleCheck+=1        
#         elif e=="{":
#             lagerCheck+=1        
#         else: 
#             if e==")" and smallCheck:
#                 smallCheck=0
#                 continue
#             elif e=="]"and middleCheck:
#                 middleCheck=0
#                 continue       
#             elif e=="}" and lagerCheck:
#                 lagerCheck=0        
#                 continue                   
#             return False
    
#     return True