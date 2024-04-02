



def isSubsequence(s,t):                    
    i=0
    j=0
    while i <len(s) and j<len(t):                
        if s[i]== t[j]:
            i+=1    
            j+=1
        else:    
            j+=1    
    
    if i==len(s):
        return True
    else:
        return False        
        
                    


s="abc"
t="ahbgdc"
print(isSubsequence(s,t))


s="axc"
t="ahbgdc"
print(isSubsequence(s,t))

