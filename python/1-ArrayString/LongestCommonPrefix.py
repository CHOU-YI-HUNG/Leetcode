def longest(strs):
    ans=""    
    minLength=len(strs[0])
    j=0
    while j<minLength:
        flag=True   
        for i in range(len(strs)-1):            
            if len(strs[i+1])<minLength:
                minLength=len(strs[i+1])  
                if minLength==0:                    
                    break                   
            flag=flag and (strs[i][j]==strs[i+1][j])
        if minLength==0:                    
            break       
        elif flag==True:
            ans+=strs[0][j]
        else:
            break    
        j+=1    
    return ans


strs=["flower","flow","flight"]
print(longest(strs))
strs=["dog","racecar","car"]
print(longest(strs))
strs=["abab","aba",""]
print(longest(strs))
