

def simplifyPath(path):
    stack = []
    directories = path.split("/")
    for dir in directories:
        if dir == "." or not dir:
            continue
        elif dir == "..":
            if stack:
                stack.pop()
        else:
            stack.append(dir)
    return "/" + "/".join(stack)




# path="/home/"
# print(simplifyPath(path))

# path="/../"
# print(simplifyPath(path))

# path="/home//foo/"
# print(simplifyPath(path))    

# path="/a/./b/../../c/"
# print(simplifyPath(path))    



path="/a/../../b/../c//.//"
print(simplifyPath(path)) 

path="/a//b////c/d//././/.."
print(simplifyPath(path)) 

path="/..."
print(simplifyPath(path)) 
path="/..hidden"
print(simplifyPath(path)) 

# def simplifyPath( path):        
    # stack=[]
    # i=1
    # temp=""
    # while i<len(path):                        
    #     if path[i]=="/":
    #         if len(temp)>0:
    #             stack.append(temp)
    #         temp=""                                    
    #     else:
    #         if i+2<len(path) and path[i]=="." and path[i+1]=="."and path[i+2]!="/":                                                  
    #             stack.append(path[i:])
    #             i+=3
    #             continue
    #         elif i+1<len(path) and path[i]=="." and path[i+1]==".":
    #             if stack:
    #                 stack.pop()
    #             i+=2
    #             continue                
    #         elif path[i]==".":
    #             i+=1
    #             continue                 
    #         temp+=path[i]                                
    #     i+=1
        
    # return "/"+"/".join(stack)